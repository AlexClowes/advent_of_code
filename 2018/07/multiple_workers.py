from collections import defaultdict
import re


def time_to_finish(prerequisites, n_workers):
    free_workers = n_workers
    in_progress = {}
    unfinished_tasks = sorted(prerequisites.keys())
    time = 0
    while unfinished_tasks:
        # Handle any completed tasks
        finished_tasks = set(
            task for task, complete_time in in_progress.items() if complete_time == time
        )
        free_workers += len(finished_tasks)
        for task in finished_tasks:
            del in_progress[task]
        for prereq in prerequisites.values():
            prereq -= finished_tasks
        # Try to start new tasks
        next_time = min(in_progress.values()) if in_progress else float("inf")
        for i, task in enumerate(unfinished_tasks):
            if free_workers == 0:
                break
            if not prerequisites[task]:
                free_workers -= 1
                complete_time = time + 61 + ord(task) - ord("A")
                in_progress[task] = complete_time
                del unfinished_tasks[i]
                next_time = min(complete_time, next_time)
        time = next_time
    return max(in_progress.values())


def main():
    with open("prerequisites.txt") as f:
        prerequisites = defaultdict(set)
        for line in sorted(f):
            prereq, task = re.match(
                "Step (\w) must be finished before step (\w) can begin.", line.strip()
            ).groups()
            prerequisites[prereq]
            prerequisites[task].add(prereq)
    print(time_to_finish(prerequisites, 5))


if __name__ == "__main__":
    main()
