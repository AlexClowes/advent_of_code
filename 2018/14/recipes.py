def next_10(n_recipes):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    while len(recipes) < 10 + n_recipes:
        n = recipes[elf1] + recipes[elf2]
        recipes += [int(d) for d in str(n)]
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    return "".join(str(d) for d in recipes[n_recipes : n_recipes + 10])


def first_appearance(pattern):
    pattern = [int(d) for d in str(pattern)]
    pattern_len = len(pattern)
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    recipe_count = 2
    while True:
        n = recipes[elf1] + recipes[elf2]
        for d in map(int, str(n)):
            recipes.append(d)
            recipe_count += 1
            if recipes[-pattern_len:] == pattern:
                return recipe_count - pattern_len
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)


def main():
    print(next_10(360781))
    print(first_appearance(360781))


if __name__ == "__main__":
    main()
