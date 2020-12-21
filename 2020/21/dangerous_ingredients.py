def main():
    allergen_map = {}
    all_ingredients = []
    with open("allergens.txt") as f:
        for line in f:
            ingredients, allergens = line.strip()[:-1].split(" (contains ")
            ingredients = ingredients.split(" ")
            all_ingredients += ingredients
            for allergen in allergens.split(", "):
                if allergen in allergen_map:
                    allergen_map[allergen] &= set(ingredients)
                else:
                    allergen_map[allergen] = set(ingredients)

    dangerous_ingredients = []
    while allergen_map:
        for allergen, possible_ingredients in allergen_map.items():
            if len(possible_ingredients) == 1:
                break
        dangerous = possible_ingredients.pop()
        dangerous_ingredients.append((allergen, dangerous))
        allergen_map.pop(allergen)
        for possible_ingredients in allergen_map.values():
            possible_ingredients.discard(dangerous)
    print(",".join(dangerous for allergen, dangerous in sorted(dangerous_ingredients)))


if __name__ == "__main__":
    main()
