from collections import defaultdict
from math import ceil
import re


def get_recipes(fname):
    with open(fname) as f:
        recipes = {}
        pat = "(\d+) (\w+)"
        for line in f:
            *inputs, output = (
                (material, int(quantity))
                for quantity, material in re.findall(pat, line)
            )
            recipes[output[0]] = (output[1], inputs)
    return recipes


def fuel_cost(recipes, quantity):
    ore = 0
    available = defaultdict(int)

    def create(material, quantity):
        nonlocal ore
        if material == "ORE":
            ore += quantity
            available["ORE"] += quantity
        else:
            out_quant, inputs = recipes[material]
            n_reactions = ceil(quantity / out_quant)
            for in_mat, in_quant in inputs:
                if n_reactions * in_quant > available[in_mat]:
                    create(in_mat, n_reactions * in_quant - available[in_mat])
                available[in_mat] -= n_reactions * in_quant
            available[material] += n_reactions * out_quant

    create("FUEL", quantity)
    return ore


def main():
    recipes = get_recipes("recipes.txt")
    print(fuel_cost(recipes, 1))


if __name__ == "__main__":
    main()
