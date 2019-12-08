from collections import defaultdict
import re

import numpy as np


def get_timesheet(logs):
    timesheet = defaultdict(lambda: np.zeros(60))
    for log in logs:
        minute = int(re.search(r":(\d+)]", log).group(1))
        if log.endswith("begins shift"):
            guard_id = int(re.search(r"#(\d+)", log).group(1))
        elif log.endswith("falls asleep"):
            sleep_start = minute
        elif log.endswith("wakes up"):
            timesheet[guard_id][sleep_start:minute] += 1
    return timesheet


def main():
    with open("times.txt") as f:
        logs = [line.strip() for line in f]
        logs.sort()
        timesheet = get_timesheet(logs)

    # Strategy 1
    worst_guard = max(timesheet, key=lambda guard_id: np.sum(timesheet[guard_id]))
    print(worst_guard * np.argmax(timesheet[worst_guard]))

    # Strategy 2
    worst_guard = max(timesheet, key=lambda guard_id: np.max(timesheet[guard_id]))
    print(worst_guard * np.argmax(timesheet[worst_guard]))


if __name__ == "__main__":
    main()
