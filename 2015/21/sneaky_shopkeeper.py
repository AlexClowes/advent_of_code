from collections import namedtuple
from itertools import chain, combinations


Item = namedtuple("Item", ["cost", "damage", "armor"])

weapons = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0),
]
armors = [
    Item(0, 0, 0),
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5),
]
rings = [
    Item(0, 0, 0),
    Item(0, 0, 0),
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3),
]


def player_wins(items, boss_stats):
    boss_health, boss_damage, boss_armor = 109, 8, 2
    player_damage = sum(item.damage for item in items)
    player_armor = sum(item.armor for item in items)
    player_health = 100
    while True:
        # Player attacks
        boss_health -= max(1, player_damage - boss_armor)
        if boss_health < 0:
            return True
        # Boss attacks
        player_health -= max(1, boss_damage - player_armor)
        if player_health < 0:
            return False


def main():
    boss_stats = {"health": 109, "damage": 8, "armor": 2}
    max_cost = 0
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in combinations(rings, 2):
                items = (weapon, armor, ring1, ring2)
                cost = sum(item.cost for item in items)
                if cost > max_cost and not player_wins(items, boss_stats):
                    max_cost = cost
    print(max_cost)


if __name__ == "__main__":
    main()
