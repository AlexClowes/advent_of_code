from collections import deque
import copy
from itertools import chain, combinations
import re


def is_safe(floor):
    for element, obj_type in floor:
        if (
            obj_type == "microchip"
            and (element, "generator") not in floor
            and any(ot == "generator" for el, ot in floor)
        ):
            return False
    return True


def main():
    with open("locations.txt") as f:
        pat = r"(\w+)(?:-compatible)? (generator|microchip)"
        items = {floor: set(re.findall(pat, line)) for floor, line in enumerate(f, 1)}

    prev_states = set()
    q = deque()
    q.append((0, 1, items))
    while q:
        n_moves, lift_pos, items = q.popleft()
        hashable_state = (lift_pos, tuple(map(tuple, items.values())))
        if hashable_state in prev_states:
            continue
        prev_states.add(hashable_state)
        if all(not items[floor] for floor in (1, 2, 3)):
            ret = n_moves
            break
        for next_lift_pos in (lift_pos - 1, lift_pos + 1):
            if next_lift_pos in (0, 5):
                continue
            for lift_contents in chain(combinations(items[lift_pos], 1), combinations(items[lift_pos], 2)):
                lift_contents = set(lift_contents)
                left_behind = items[lift_pos] - lift_contents
                with_cargo = items[next_lift_pos] | lift_contents
                if is_safe(left_behind) and is_safe(with_cargo):
                    new_items = copy.deepcopy(items)
                    new_items[lift_pos] = left_behind
                    new_items[next_lift_pos] = with_cargo
                    q.append((n_moves + 1, next_lift_pos, new_items))

    print(ret)
    # Adding two extra pairs on floor 1 costs 24 extra moves
    print(ret + 24)


if __name__ == "__main__":
    main()
