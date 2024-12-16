from heapq import heappop, heappush


def main():
    with open("map.txt") as f:
        walls = set()
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                if char == "#":
                    walls.add((i, j))
                elif char == "S":
                    start = (i, j)
                elif char == "E":
                    end = (i, j)

    def get_paths():
        best_score = float("inf")
        q = [(0, start, (0, 1), (start))]
        seen = {}
        while q:
            score, pos, heading, path = heappop(q)
            if pos == end:
                best_score = score
                yield path
            if score > best_score or seen.get((pos, heading), float("inf")) < score:
                continue
            seen[pos, heading] = score
            for new_score, new_pos, new_heading in (
                (score + 1, (pos[0] + heading[0], pos[1] + heading[1]), heading),
                (score + 1000, pos, (-heading[1], heading[0])),
                (score + 1000, pos, (heading[1], -heading[0])),
            ):
                if new_pos not in walls:
                    heappush(q, (new_score, new_pos, new_heading, path + (new_pos,)))

    visited = set.union(*(set(path) for path in get_paths()))

    print(len(visited) - 2)


if __name__ == "__main__":
    main()
