import re


class Reindeer:
    def __init__(self, fly_speed, fly_time, rest_time):
        self.fly_speed = fly_speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.flying = True
        self.time_to_switch = fly_time
        self.dist = 0
        self.score = 0

    def update_dist(self):
        self.time_to_switch -= 1
        if self.flying:
            self.dist += self.fly_speed
        if self.time_to_switch == 0:
            self.flying = not self.flying
            self.time_to_switch = self.fly_time if self.flying else self.rest_time


def main():
    pat = r"\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    with open("reindeer.txt") as f:
        reindeers = [Reindeer(*map(int, args)) for args in re.findall(pat, f.read())]

    for t in range(2503):
        for rd in reindeers:
            rd.update_dist()
        max_dist = max(rd.dist for rd in reindeers)
        for rd in reindeers:
            if rd.dist == max_dist:
                rd.score += 1
    print(max(rd.score for rd in reindeers))


if __name__ == "__main__":
    main()
