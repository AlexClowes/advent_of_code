import copy
from itertools import count
import re


class Group:
    def __init__(
        self,
        number,
        hit_points,
        damage,
        damage_type,
        initiative,
        weaknesses=(),
        immunities=(),
    ):
        self.number = number
        self.hit_points = hit_points
        self.damage = damage
        self.damage_type = damage_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

    @property
    def effective_power(self):
        return self.number * self.damage


def expected_damage(attacker, defender):
    if attacker.damage_type in defender.immunities:
        return 0
    if attacker.damage_type in defender.weaknesses:
        return 2 * attacker.effective_power
    return attacker.effective_power


def try_int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return x


def get_groups(f):
    while line := f.readline().strip():
        kwargs = {}
        kwargs.update(
            re.match(
                r"(?P<number>\d+) units each with (?P<hit_points>\d+) hit points", line
            ).groupdict()
        )
        if match := re.search(r"weak to (\w+(?:,\s\w+)*)", line):
            kwargs["weaknesses"] = match.group(1).split(", ")
        if match := re.search(r"immune to (\w+(?:,\s\w+)*)", line):
            kwargs["immunities"] = match.group(1).split(", ")
        kwargs.update(
            re.search(
                r"with an attack that does (?P<damage>\d+) (?P<damage_type>\w+) damage at initiative (?P<initiative>\d+)",
                line,
            ).groupdict()
        )
        kwargs = {k: try_int(v) for k, v in kwargs.items()}
        yield Group(**kwargs)


def fight(immune_groups, infection_groups):
    # Target selection
    selection_order = sorted(
        immune_groups | infection_groups,
        key=lambda group: (group.effective_power, group.initiative),
        reverse=True,
    )
    already_attacked = set()
    attack_queue = []
    for attacker in selection_order:
        defenders = immune_groups if attacker in infection_groups else infection_groups
        defender = max(
            defenders - already_attacked,
            key=lambda d: (
                expected_damage(attacker, d),
                d.effective_power,
                d.initiative,
            ),
            default=None,
        )
        if defender is not None and expected_damage(attacker, defender) > 0:
            attack_queue.append((attacker, defender))
            already_attacked.add(defender)

    # Attack
    attack_queue = sorted(attack_queue, key=lambda ad: ad[0].initiative, reverse=True)
    dead = set()
    stalemate = True
    for attacker, defender in attack_queue:
        if attacker not in dead:
            units_killed = expected_damage(attacker, defender) // defender.hit_points
            if units_killed > 0:
                stalemate = False
            defender.number -= units_killed
            if defender.number <= 0:
                dead.add(defender)
    # Remove killed groups
    immune_groups = immune_groups - dead
    infection_groups = infection_groups - dead
    # Check if fight is over - either because one side has lost, or a stalemate
    # has occurred.
    done = stalemate or not immune_groups or not infection_groups
    return immune_groups, infection_groups, done


def result(immune_groups, infection_groups, boost=0):
    immune_groups = copy.deepcopy(immune_groups)
    infection_groups = copy.deepcopy(infection_groups)
    for group in immune_groups:
        group.damage += boost
    done = False
    while not done:
        immune_groups, infection_groups, done = fight(immune_groups, infection_groups)
    total = lambda groups: sum(group.number for group in groups)
    return total(immune_groups), total(infection_groups)


def main():
    with open("condition.txt") as f:
        assert f.readline() == "Immune System:\n"
        immune_groups = set(get_groups(f))
        assert f.readline() == "Infection:\n"
        infection_groups = set(get_groups(f))

    # Part 1
    print(result(immune_groups, infection_groups)[1])

    # Part 2
    for boost in count():
        imm_total, inf_total = result(immune_groups, infection_groups, boost)
        if imm_total > 0 and inf_total == 0:
            print(imm_total)
            break


if __name__ == "__main__":
    main()
