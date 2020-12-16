from itertools import chain
import re


def is_valid(ticket, field_ranges):
    return all(
        any(n in r for r in chain.from_iterable(field_ranges.values())) for n in ticket
    )


def get_field_positions(tickets, field_ranges):
    # First use field ranges and nearby ticket values to constrain the set of
    # fields for each position
    n_fields = len(field_ranges)
    possible_fields = {pos: set(field_ranges) for pos in range(n_fields)}
    for ticket in tickets:
        for pos, val in enumerate(ticket):
            possible_fields[pos] = {
                field
                for field in possible_fields[pos]
                if any(val in r for r in field_ranges[field])
            }

    # If a position has only one possible field, then we can remove that field
    # from the possibilities of every other position. Repeat until every position
    # has only one possible field
    sorted_positions = sorted(possible_fields, key=lambda p: len(possible_fields[p]))
    for i, pos in enumerate(sorted_positions):
        assert len(possible_fields[pos]) == 1
        for pos2 in sorted_positions[i + 1 :]:
            possible_fields[pos2] -= possible_fields[pos]

    return {fields.pop(): pos for pos, fields in possible_fields.items()}


def main():
    field_ranges = {}
    # with open("ex2.txt") as f:
    with open("tickets.txt") as f:
        # Get field ranges
        while (line := f.readline()) != "\n":
            pat = r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)"
            field, lo1, hi1, lo2, hi2 = re.match(pat, line).groups()
            lo1, hi1, lo2, hi2 = map(int, (lo1, hi1, lo2, hi2))
            field_ranges[field] = (range(lo1, hi1 + 1), range(lo2, hi2 + 1))

        # My ticket
        assert f.readline() == "your ticket:\n"
        my_ticket = [int(n) for n in f.readline().strip().split(",")]
        assert f.readline() == "\n"

        # Nearby tickets
        assert f.readline() == "nearby tickets:\n"
        nearby_tickets = (list(map(int, line.strip().split(","))) for line in f)
        valid_tickets = (
            ticket for ticket in nearby_tickets if is_valid(ticket, field_ranges)
        )

        field_positions = get_field_positions(valid_tickets, field_ranges)

    prod = 1
    for field, pos in field_positions.items():
        if field.startswith("departure"):
            prod *= my_ticket[pos]
    print(prod)


if __name__ == "__main__":
    main()
