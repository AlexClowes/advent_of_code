from one_fuel import fuel_cost, get_recipes


def bin_search(func, lower_bound, upper_bound):
    mid_point = (lower_bound + upper_bound) // 2
    fm = func(mid_point)
    if fm <= 0 and func(mid_point + 1) > 0:
        return mid_point
    elif fm < 0:
        return bin_search(func, mid_point, upper_bound)
    elif fm > 0:
        return bin_search(func, lower_bound, mid_point)


def main():
    recipes = get_recipes("recipes.txt")
    print(bin_search(lambda x: fuel_cost(recipes, x) - 10 ** 12, 1, 10 ** 10))


if __name__ == "__main__":
    main()
