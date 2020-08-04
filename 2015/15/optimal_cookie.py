import re

def prod(iterator):
    ret = 1
    for el in iterator:
        ret *= el
    return ret


def clip(x):
    return x if x > 0 else 0


def dot_prod(x, y):
    return sum(a * b for a, b in zip(x, y))


def main():
    pat = r"\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories -?\d+"
    parameters = [[] for _ in range(4)]
    with open("ingredients.txt") as f:
        ingredients = [line.strip() for line in f]
    for line in ingredients:
        for param, val in zip(parameters, re.match(pat, line).groups()):
            param.append(int(val))

    def score(*quantities):
        return prod(clip(dot_prod(p, quantities)) for p in parameters)

    max_score = 0
    for a in range(100):
        for b in range(100 - a):
            for c in range(100 - a - b):
                d = 100 - a - b - c
                max_score = max(max_score, score(a, b, c, d))
    print(max_score)


if __name__ == "__main__":
    main()
