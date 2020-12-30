from functools import lru_cache
import heapq


def adj(i, j):
    if i > 0:
        yield i - 1, j
    yield i + 1, j
    if j > 0:
        yield i, j - 1
    yield i, j + 1


def main():
    depth = 9465
    target = (13, 704)

    def geologic_index(x, y):
        if (x, y) == target:
            return 0
        if x == 0:
            return 48271 * y
        if y == 0:
            return 16807 * x
        return (erosion_level(x - 1, y) * erosion_level(x, y - 1)) % 20183

    @lru_cache(maxsize=None)
    def erosion_level(x, y):
        return (geologic_index(x, y) + depth) % 20183

    def dist(x, y):
        return abs(x - target[0]) + abs(y - target[0])

    # Find best route
    allowed_tools = {0: "TC", 1: "CN", 2: "TN"}
    best_time = float("inf")
    earliest_time = {}
    q = [(dist(0, 0), 0, (0, 0), "T")]
    while q:
        priority, time, pos, tool = heapq.heappop(q)
        if pos == target and tool == "T":
            best_time = min(best_time, time)
        if time < best_time and earliest_time.get((pos, tool), float("inf")) > time:
            earliest_time[pos, tool] = time
            # Try to move to adjacent squares
            for new_pos in adj(*pos):
                if tool in allowed_tools[erosion_level(*new_pos) % 3]:
                    heapq.heappush(q, (dist(*new_pos), time + 1, new_pos, tool))
            # Try to change tools
            for new_tool in allowed_tools[erosion_level(*pos) % 3]:
                if tool != new_tool:
                    heapq.heappush(q, (priority, time + 7, pos, new_tool))
    print(best_time)


if __name__ == "__main__":
    main()
