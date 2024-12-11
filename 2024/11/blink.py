from functools import cache


@cache
def update(stone):
    if stone == 0:
        return [1]
    elif len(stone_str := str(stone)) % 2 == 0:
        mid = len(stone_str) // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]
    else:
        return [stone * 2024]


@cache
def stone_count(stone, blinks):
    if blinks == 0:
        return 1
    return sum(stone_count(new_stone, blinks - 1) for new_stone in update(stone))


def main():
    with open("stones.txt") as f:
        stones = [int(n) for n in f.read().strip().split()]

    print(sum(stone_count(stone, 25) for stone in stones))
    print(sum(stone_count(stone, 75) for stone in stones))


if __name__ == "__main__":
    main()
