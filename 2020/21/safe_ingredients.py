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

    unsafe_ingredients = set.union(*allergen_map.values())
    print(sum(ingredient not in unsafe_ingredients for ingredient in all_ingredients))


if __name__ == "__main__":
    main()
