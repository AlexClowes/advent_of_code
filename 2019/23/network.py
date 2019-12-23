from collections import defaultdict

from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    # Launch computers
    computers = [launch_int_code_computer(program) for _ in range(50)]

    # Set addresses
    for idx, (in_queue, _) in enumerate(computers):
        in_queue.put(idx)

    # Run network
    while True:
        # Collect outputs
        stored_outputs = defaultdict(list)
        for _, out_queue in computers:
            if out_queue.qsize():
                addr = out_queue.get()
                for _ in range(2):
                    stored_outputs[addr].append(out_queue.get())
        # Check for termination condition
        if stored_outputs[255]:
            print(stored_outputs[255][1])
            break
        # Send outputs to computers
        for idx, (in_queue, _) in enumerate(computers):
            for val in stored_outputs[idx]:
                in_queue.put(val)
            if not stored_outputs[idx]:
                in_queue.put(-1)

    # Terminate computers
    for in_queue, _ in computers:
        in_queue.put(StopIteration)


if __name__ == "__main__":
    main()
