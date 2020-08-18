from collections import defaultdict
import re


def top_sort(prerequisites):
    unfinished_tasks = sorted(prerequisites.keys())
    while unfinished_tasks:
        for i, task in enumerate(unfinished_tasks):
            if not prerequisites[task]:
                yield task
                del unfinished_tasks[i]
                for prereq in prerequisites.values():
                    if task in prereq:
                        prereq.remove(task)
                break


def main():
    with open("prerequisites.txt") as f:
        prerequisites = defaultdict(set)
        for line in sorted(f):
            prereq, task = re.match(
                "Step (\w) must be finished before step (\w) can begin.", line.strip()
            ).groups()
            prerequisites[prereq]
            prerequisites[task].add(prereq)
    print("".join(top_sort(prerequisites)))


if __name__ == "__main__":
    main()
