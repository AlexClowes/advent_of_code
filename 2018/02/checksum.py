from collections import Counter


def checksum(box_ids):
    char_counts = [Counter(box_id) for box_id in box_ids]
    doubles = sum(2 in count.values() for count in char_counts)
    triples = sum(3 in count.values() for count in char_counts)
    return doubles * triples


def main():
    with open("box_ids.txt") as f:
        box_ids = (line.strip() for line in f)
        print(checksum(box_ids))


if __name__ == "__main__":
    main()
