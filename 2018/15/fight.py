from collections import deque
from itertools import chain, count

import numpy as np


class Unit:
    def __init__(self, race, pos, attack_power):
        self.race = race
        self.pos = pos
        self.attack_power = attack_power
        self.hit_points = 200


def adj(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_victim(attacker, targets):
    in_range = [t for t in targets if dist(attacker.pos, t.pos) == 1]
    if in_range:
        return min(in_range, key=lambda t: (t.hit_points, t.pos))


def move_choices(start_pos, destinations, battle_map):
    q = deque()
    for adj_pos in adj(*start_pos):
        if battle_map[adj_pos] == ".":
            q.append((adj_pos, 1, adj_pos))
    min_steps = float("inf")
    seen = {}
    while q:
        pos, n_steps, first_step = q.popleft()
        if n_steps > min_steps:
            break
        if pos in seen and seen[pos] <= (n_steps, first_step):
            continue
        seen[pos] = (n_steps, first_step)
        if pos in destinations:
            yield n_steps, pos, first_step
            min_steps = n_steps
            continue
        for new_pos in adj(*pos):
            if battle_map[new_pos] == ".":
                q.append((new_pos, n_steps + 1, first_step))


def move(unit, targets, battle_map):
    squares_in_range = chain.from_iterable(adj(*t.pos) for t in targets)
    destinations = set(s for s in squares_in_range if battle_map[s] == ".")
    legal_moves = list(move_choices(unit.pos, destinations, battle_map))
    if legal_moves:
        best_move = min(legal_moves)[2]
        battle_map[best_move] = battle_map[unit.pos]
        battle_map[unit.pos] = "."
        unit.pos = best_move


def outcome(battle_map, elf_strength=3):
    # Create all units
    elves = []
    goblins = []
    for i in range(battle_map.shape[0]):
        for j in range(battle_map.shape[1]):
            if battle_map[i, j] == "E":
                elves.append(Unit("Elf", (i, j), elf_strength))
            elif battle_map[i, j] == "G":
                goblins.append(Unit("Goblin", (i, j), 3))

    # Continue until one side wins
    death_count = {"Elf": 0, "Goblin": 0}
    for round in count():
        #import time; time.sleep(1 / 30)
        units = sorted(elves + goblins, key=lambda u: u.pos)
        for unit in sorted(elves + goblins, key=lambda u: u.pos):
            # Check unit is actually alive
            if unit.hit_points <= 0:
                continue
            # Identify all targets
            targets = goblins if unit.race == "Elf" else elves
            targets = [t for t in targets if t.hit_points > 0]
            # Check if for targets in range
            victim = get_victim(unit, targets)
            if not victim:
                # Try moving
                move(unit, targets, battle_map)
                # Try to get victim again
                victim = get_victim(unit, targets)
            # Attack
            if victim:
                victim.hit_points -= unit.attack_power
                if victim.hit_points <= 0:
                    battle_map[victim.pos] = "."
                    death_count[victim.race] += 1
            # Check for victory
            if all(t.hit_points <= 0 for t in targets):
                total_health = sum(max(0, u.hit_points) for u in units)
                round_no = round + (unit is units[-1])
                score = total_health * round_no
                return death_count, score


def main():
    with open("map.txt") as f:
        battle_map = np.array([list(line.strip()) for line in f])

    _, score = outcome(np.copy(battle_map))
    print(score)

    for elf_strength in count(4):
        death_count, score = outcome(np.copy(battle_map), elf_strength)
        if death_count["Elf"] == 0:
            print(score)
            break


if __name__ == "__main__":
    main()
