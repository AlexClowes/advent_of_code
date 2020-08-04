import re


def total_dist(fly_speed, fly_time, rest_time, tot_time):
    n_cycles, leftover_time = divmod(tot_time, fly_time + rest_time)
    return fly_speed * (n_cycles * fly_time + min(leftover_time, fly_time))


def main():
    pat = r"\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    with open("reindeer.txt") as f:
        max_dist = 0
        for line in f:
            args = map(int, re.match(pat, line.strip()).groups())
            dist = total_dist(*args, 2503)
            if dist > max_dist:
                max_dist = dist
    print(max_dist)


if __name__ == "__main__":
    main()
