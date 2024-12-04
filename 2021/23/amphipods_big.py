from collections import namedtuple
from functools import cache
from heapq import heappush, heappop


Loc = namedtuple("Loc", ("x", "y"))

ROOMS = [Loc(x, y) for x in (3, 5, 7, 9) for y in (1, 2, 3, 4)]
HALLS = [Loc(x, 0) for x in (1, 2, 4, 6, 8, 10, 11)]

AMPHIPOD_ROOMS = dict(A=3, B=5, C=7, D=9)
ENERGY_COST = dict(A=1, B=10, C=100, D=1000)


@cache
def dist(loc1, loc2):
    return abs(loc1.x - loc2.x) + abs(loc1.y - loc2.y)


@cache
def clear_spaces_needed(room, hall):
    return set([
        other
        for other in ROOMS
        if other.x == room.x and other.y < room.y
    ] + [
        other
        for other in HALLS
        if (
            room.x < other.x < hall.x
            or hall.x < other.x < room.x
        )
    ])


def replace(tup, idx, item):
    return tuple(sorted(tup[:idx] + tup[idx + 1:] + (item,)))


def get_new_states(energy, state):
    occupied_spaces = {space for _, space, _ in state}
    for i, (amph, loc, locked) in enumerate(state):
        if locked:
            continue
        if loc in ROOMS:
            # room -> hall
            for hall in HALLS:
                if (
                    hall not in occupied_spaces
                    and occupied_spaces.isdisjoint(clear_spaces_needed(loc, hall))
                ):
                    new_energy = energy + ENERGY_COST[amph] * dist(loc, hall)
                    new_state = replace(state, i, (amph, hall, False))
                    yield new_energy, new_state
        else:
            # hall -> room
            for room in ROOMS:
                if (
                    room.x == AMPHIPOD_ROOMS[amph]
                    and room not in occupied_spaces
                    and occupied_spaces.isdisjoint(clear_spaces_needed(room, loc))
                    and not any(
                        a != amph and l.x == room.x
                        for a, l, _ in state
                    )
                ):
                    new_energy = energy + ENERGY_COST[amph] * dist(loc, room)
                    new_state = replace(state, i, (amph, room, True))
                    yield new_energy, new_state


def main():
    with open("config.txt") as f:
        lines = [line for line in f.read().split("\n")[1:]]
        lines.insert(2, "  #D#C#B#A#")
        lines.insert(3, "  #D#B#A#C#")

    initial_state = tuple(
        sorted((lines[room.y][room.x], room, False) for room in ROOMS)
    )
    terminal_state = tuple(zip("AABBCCDD", ROOMS))

    seen = set()
    q = [(0, initial_state)]
    while q:
        energy, state = heappop(q)
        if all(
            a1 == a2 and r1 == r2
            for (a1, r1, _), (a2, r2) in zip(state, terminal_state)
        ):
            break
        if state in seen:
            continue
        seen.add(tuple(sorted(state)))
        for new_energy, new_state in get_new_states(energy, state):
            heappush(q, (new_energy, new_state))

    print(energy)


if __name__ == "__main__":
    main()
