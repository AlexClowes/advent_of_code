from collections import defaultdict
import re


def main():
    pat = r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
    particles = set()
    with open("initial_state.txt") as f:
        for line in f:
            px, py, pz, vx, vy, vz, ax, ay, az = map(int, re.match(pat, line).groups())
            particles.add(((px, py, pz), (vx, vy, vz), (ax, ay, az)))

    # Assume everything has settled after 100 iterations
    for _ in range(100):
        # Check for collisions
        positions = defaultdict(list)
        for particle in particles:
            positions[particle[0]].append(particle)
        for pos in positions:
            if len(positions[pos]) > 1:
                for particle in positions[pos]:
                    particles.remove(particle)
        # Advance particles
        new_particles = set()
        for p, v, a in particles:
            new_v = tuple(v[i] + a[i] for i in range(3))
            new_p = tuple(p[i] + new_v[i] for i in range(3))
            new_particles.add((new_p, new_v, a))
        particles = new_particles
    print(len(particles))


if __name__ == "__main__":
    main()
