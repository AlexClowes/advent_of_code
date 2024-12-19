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

    q = [(0, start, (0, 1))]
    seen = set()
    while q:
        score, pos, heading = heappop(q)
        if pos == end:
            print(score)
            return
        if (pos, heading) in seen:
            continue
        seen.add((pos, heading))
        for new_score, new_pos, new_heading in (
            (score + 1, (pos[0] + heading[0], pos[1] + heading[1]), heading),
            (score + 1000, pos, (-heading[1], heading[0])),
            (score + 1000, pos, (heading[1], -heading[0])),
        ):
            if new_pos not in walls:
                heappush(q, (new_score, new_pos, new_heading))



if __name__ == "__main__":
    main()