from collections import defaultdict
import functools
import heapq
from itertools import combinations, pairwise, permutations
import re

from tqdm import tqdm


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
        valve: 29 - get_min_dist("AA", valve)
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

    def max_flow(time, pos, seen, flow):
        ret = flow
        for new_pos in graph:
            if new_pos in seen:
                continue
            new_time = time - graph[pos][new_pos] - 1
            if new_time <= 0:
                continue
            new_seen = seen + (new_pos,)
            new_flow = flow + new_time * flow_rate[new_pos]
            ret = max(ret, max_flow(new_time, new_pos, new_seen, new_flow))
        return ret
    
    print(
        max(
            max_flow(time, valve, (valve,), time * flow_rate[valve])
            for valve, time in start_times.items()
        )
    )


if __name__ == "__main__":
    main()
