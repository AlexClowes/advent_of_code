from collections import namedtuple, deque
from itertools import islice
import re


class Resources(
    namedtuple(
        "Resources",
        ("ore", "clay", "obsidian", "geodes"),
        defaults=(0, 0, 0, 0),
    )
):
    def __add__(self, other):
        return Resources(*(x + y for x, y in zip(self, other)))

    def __sub__(self, other):
        return Resources(*(x - y for x, y in zip(self, other)))

    def __mul__(self, scale):
        return Resources(*(r * scale for r in self))

    def __gt__(self, other):
        return any(x > y for x, y in zip(self, other))


Robot = namedtuple("Robot", ("production", "cost"))


class Blueprint(namedtuple("Blueprint", ("id_no", "robots"))):
    @staticmethod
    def from_line(line):
        pat = (
            "Blueprint (\d+): "
            "Each ore robot costs (\d+) ore. "
            "Each clay robot costs (\d+) ore. "
            "Each obsidian robot costs (\d+) ore and (\d+) clay. "
            "Each geode robot costs (\d+) ore and (\d+) obsidian."
        )
        (
            id_no,
            ore_ore_cost,
            clay_ore_cost,
            obsidian_ore_cost,
            obsidian_clay_cost,
            geode_ore_cost,
            geode_obsidian_cost,
        ) = map(int, re.match(pat, line).groups())
        return Blueprint(
            id_no,
            (
                Robot(Resources(ore=1), Resources(ore=ore_ore_cost)),
                Robot(Resources(clay=1), Resources(ore=clay_ore_cost)),
                Robot(
                    Resources(obsidian=1),
                    Resources(ore=obsidian_ore_cost, clay=obsidian_clay_cost),
                ),
                Robot(
                    Resources(geodes=1),
                    Resources(ore=geode_ore_cost, obsidian=geode_obsidian_cost),
                ),
            ),
        )

    def score(self, time_limit):
        production_limits = Resources(
            ore=max(robot.cost.ore for robot in self.robots),
            clay=max(robot.cost.clay for robot in self.robots),
            obsidian=max(robot.cost.obsidian for robot in self.robots),
            geodes=float("inf"),
        )

        max_geodes = 0
        q = deque()
        q.append((time_limit, Resources(), Resources(ore=1)))
        while q:
            time, resources, production = q.popleft()
            if time == 0:
                if resources.geodes > max_geodes:
                    max_geodes = resources.geodes
                continue
            # If even building one geode bot per minute won't catch up, then
            # stop
            if (
                resources.geodes
                + time * production.geodes
                + time * (time - 1) // 2
            ) < max_geodes:
                continue
            # Try building each type of robot, waiting if we don't have enough
            # resources yet
            for idx, robot in enumerate(self.robots):
                # If we already have more of a resource than we can use, then
                # don't bother building another robot to produce it
                if (
                    resources[idx]
                    + time * (production[idx] - production_limits[idx])
                ) >= 0:
                    continue
                new_time = time
                new_resources = resources
                while new_time > 0 and robot.cost > new_resources:
                    new_time -= 1
                    new_resources += production
                if new_time == 0:
                    q.append((0, new_resources, production))
                else:
                    new_time -= 1
                    new_resources += production - robot.cost
                    new_production = production + robot.production
                    q.append((new_time, new_resources, new_production))

        return max_geodes


def product(iterable):
    p = 1
    for el in iterable:
        p *= el
    return p


def main():
    pat = (
        "Blueprint (\d+): "
        "Each ore robot costs (\d+) ore. "
        "Each clay robot costs (\d+) ore. "
        "Each obsidian robot costs (\d+) ore and (\d+) clay. "
        "Each geode robot costs (\d+) ore and (\d+) obsidian."
    )
    with open("blueprints.txt") as f:
        print(
            product(
                Blueprint.from_line(line.strip()).score(32)
                for line in islice(f, 3)
            )
        )


if __name__ == "__main__":
    main()
