from itertools import chain
import json


def flatten(data):
    if isinstance(data, dict):
        yield from chain.from_iterable(map(flatten, data.keys()))
        yield from chain.from_iterable(map(flatten, data.values()))
    elif isinstance(data, list):
        yield from chain.from_iterable(map(flatten, data))
    else:
        yield data



def main():
    with open("input.json") as f:
        data = json.load(f)

    print(sum(filter(lambda x: isinstance(x, int), flatten(data))))


if __name__ == "__main__":
    main()
