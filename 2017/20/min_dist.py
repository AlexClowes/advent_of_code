import re


def main():
    pat = r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
    with open("initial_state.txt") as f:
        min_dist_coefs = (float("inf"),) * 3
        for particle, line in enumerate(f):
            initial_state = [abs(int(x)) for x in re.match(pat, line).groups()]
            dist_coefs = (sum(initial_state[6:]), sum(initial_state[3:6]), sum(initial_state[:3]))
            if dist_coefs < min_dist_coefs:
                min_dist_coefs = dist_coefs
                min_particle = particle
    print(min_particle)


if __name__ == "__main__":
    main()
