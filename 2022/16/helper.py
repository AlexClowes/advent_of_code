from collections import defaultdict, namedtuple
import functools
import heapq
from itertools import combinations, pairwise, permutations
import re


def main():
    pat = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([,\s\w]+)"

    flow_rate = {}
    graph = defaultdict(dict)

    with open("valves.txt") as f:
        for line in f:
            valve, rate, tunnels = re.match(pat, line.strip()).groups()
            flow_rate[valve] = int(rate)
            for other_valve in tunnels.split(", "):
                graph[valve][other_valve] = 1

    def get_min_dist(start, dest):
        seen = set()
        q = [(0, start)]
        while q:
            total_dist, pos = heapq.heappop(q)
            if pos == dest:
                return total_dist
            if pos not in seen:
                seen.add(pos)
                for new_pos, dist in graph[pos].items():
                    heapq.heappush(q, (total_dist + dist, new_pos))

    start_times = {
        valve: 25 - get_min_dist("AA", valve)
        for valve, flow in flow_rate.items()
        if flow
    }

    # Make graph connected
    for v1, v2 in combinations(list(graph), 2):
        if (v1 == "AA" or flow_rate[v1]) and flow_rate[v2]:
            graph[v1][v2] = graph[v2][v1] = get_min_dist(v1, v2)

    # Prune valves with no flow rate
    for v1 in list(graph):
        if not flow_rate[v1]:
            for v2 in graph[v1]:
                del graph[v2][v1]
            del graph[v1]

    def max_flow(time1, pos1, time2, pos2, seen, flow):
        if time1 == time2 == 0:
            return flow
        if time1 < time2:
            return max_flow(time2, pos2, time1, pos1, seen, flow)
        # Base case is that worker at pos1 stops there forever
        ret = max_flow(time2, pos2, 0, pos1, seen, flow)
        # See if we can do better than base case by having worker at pos1 move
        for new_pos1 in graph:
            if new_pos1 in seen:
                continue
            new_time1 = time1 - graph[pos1][new_pos1] - 1
            if new_time1 <= 0:
                continue
            new_seen = seen + (new_pos1,)
            new_flow = flow + new_time1 * flow_rate[new_pos1]
            ret = max(ret, max_flow(new_time1, new_pos1, time2, pos2, new_seen, new_flow))
        return ret

    result = 1
    for (v1, t1), (v2, t2) in combinations(start_times.items(), 2):
        result = max(result, max_flow(t1, v1, t2, v2, (v1, v2), t1 * flow_rate[v1] + t2 * flow_rate[v2]))
    print(result)


if __name__ == "__main__":
    main()
