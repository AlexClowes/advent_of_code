from itertools import permutations


def main():
    with open("city_map.txt") as f:
        city_map = [line.strip() for line in f]
    n_cities = int((1 + (1 + 8 * len(city_map)) ** 0.5) // 2)
    distances = (int(line.split()[-1]) for line in city_map)
    dist = [[0] * n_cities for _ in range(n_cities)]
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
            dist[i][j] = dist[j][i] = next(distances)

    routes = permutations(range(n_cities))
    route_lens = (sum(dist[c1][c2] for c1, c2 in zip(r[:-1], r[1:])) for r in routes)

    min_route, max_route = float("inf"), 0
    for route_len in route_lens:
        min_route = min(route_len, min_route)
        max_route = max(route_len, max_route)

    print(min_route)
    print(max_route)


if __name__ == "__main__":
    main()

