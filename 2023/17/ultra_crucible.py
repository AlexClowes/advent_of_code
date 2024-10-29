import heapq


def main():
    with open("cooling_map.txt") as f:
        grid = [[int(char) for char in line.strip()] for line in f]
    i_max = len(grid)
    j_max = len(grid[0])

    start = (0, 0)
    end = (i_max - 1, j_max - 1)

    seen = set()
    queue = [(0, *start, 1, 0), (0, *start, 0, 1)]
    while queue:
        heat_loss, i, j, di, dj = heapq.heappop(queue)

        if (i, j) == end:
            print(heat_loss)
            return

        if (i, j, di, dj) in seen:
            continue
        seen.add((i, j, di, dj))


        for (new_di, new_dj) in ((-dj, di), (dj, -di)):
            new_i, new_j = i, j
            new_heat_loss = heat_loss
            for steps in range(1, 11):
                new_i += new_di
                new_j += new_dj
                if 0 <= new_i < i_max and 0 <= new_j < j_max:
                    new_heat_loss += grid[new_i][new_j]
                    if steps >= 4:
                        heapq.heappush(queue, (new_heat_loss, new_i, new_j, new_di, new_dj))
                else:
                    break


if __name__ == "__main__":
    main()
