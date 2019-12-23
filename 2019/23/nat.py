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
    nat_memory = None
    seen_y_vals = set()
    while True:
        # Collect outputs
        stored_outputs = defaultdict(list)
        idle = True
        for _, out_queue in computers:
            if out_queue.qsize():
                idle = False
                addr = out_queue.get()
                for _ in range(2):
                    stored_outputs[addr].append(out_queue.get())
        # Check for update to nat memory
        if stored_outputs[255]:
            nat_memory = stored_outputs[255]
        # Send outputs to computers
        for idx, (in_queue, _) in enumerate(computers):
            for val in stored_outputs[idx]:
                in_queue.put(val)
            if not stored_outputs[idx]:
                in_queue.put(-1)
        # Send nat memory to computer 0
        if idle and nat_memory:
            if nat_memory[1] in seen_y_vals:
                print(nat_memory[1])
                break
            seen_y_vals.add(nat_memory[1])
            for val in nat_memory:
                computers[0][0].put(val)
            nat_memory = None

    # Terminate computers
    for in_queue, _ in computers:
        in_queue.put(StopIteration)


if __name__ == "__main__":
    main()
