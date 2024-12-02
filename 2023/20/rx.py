from collections import deque, namedtuple
from enum import Enum
from itertools import combinations


Pulse = Enum("Pulse", ("LOW", "HIGH"))
Event = namedtuple("Event", ("source", "dest", "pulse"))
ModuleType = Enum("ModuleType", ("BROADCASTER", "FLIPFLOP", "CONJUNCTION"))
ModuleSpec = namedtuple("ModuleSpec", ("type", "state"))


def parse(module_spec_str):
    name, destinations = module_spec_str.strip().split(" -> ")
    destinations = destinations.split(", ")
    if name == "broadcaster":
        spec = ModuleSpec(ModuleType.BROADCASTER, None)
    elif name.startswith("%"):
        name = name[1:]
        spec = ModuleSpec(ModuleType.FLIPFLOP, {"active": False})
    elif name.startswith("&"):
        name = name[1:]
        spec = ModuleSpec(ModuleType.CONJUNCTION, {})
    return name, destinations, spec


def process(module, event):
    if module.type == ModuleType.BROADCASTER:
        return event.pulse
    elif module.type == ModuleType.FLIPFLOP:
        if event.pulse is Pulse.HIGH:
            return None
        module.state["active"] = not module.state["active"]
        return Pulse.HIGH if module.state["active"] else Pulse.LOW
    elif module.type == ModuleType.CONJUNCTION:
        module.state[event.source] = event.pulse
        return (
            Pulse.LOW
            if all(pulse is Pulse.HIGH for pulse in module.state.values())
            else Pulse.HIGH
        )


def main():
    network = {}
    modules = {}
    with open("module_config.txt") as f:
        for line in f:
            name, destinations, spec = parse(line.strip())
            network[name] = destinations
            modules[name] = spec
    for source, destinations in network.items():
        for dest in destinations:
            if dest in modules and modules[dest].type == ModuleType.CONJUNCTION:
                modules[dest].state[source] = Pulse.LOW

    def get_inputs(node):
        return [inp for inp, destinations in network.items() if node in destinations]

    # Check only one node feeds into rx and that node is a conjuction module
    rx_input, = get_inputs("rx")
    assert modules[rx_input].type == ModuleType.CONJUNCTION

    # Check that network can be partitioned and each sub-network provides exactly one
    # input to rx_input
    def bfs(start):
        seen = set()
        q = deque([start])
        while q:
            pos = q.popleft()
            if pos in seen:
                continue
            if pos in network:
                seen.add(pos)
                q.extend(network[pos])
        return seen

    partitions = [bfs(node) for node in network["broadcaster"]]
    assert len(get_inputs(rx_input)) == len(partitions)
    for nodes1, nodes2 in combinations(partitions, 2):
        assert nodes1 & nodes2 == {rx_input}

    nodes_to_watch = set(get_inputs(rx_input))
    watched_node_first_high = []

    event_queue = deque([])

    button_presses = 0
    while nodes_to_watch:
        button_presses += 1
        event_queue.append(Event("button", "broadcaster", Pulse.LOW))
        while event_queue:
            event = event_queue.popleft()
            if event.source in nodes_to_watch and event.pulse is Pulse.HIGH:
                nodes_to_watch.remove(event.source)
                watched_node_first_high.append(button_presses)
            if (module := modules.get(event.dest)) and (pulse := process(module, event)):
                event_queue.extend(
                    Event(event.dest, dest, pulse) for dest in network[event.dest]
                )
    prod = 1
    for x in watched_node_first_high:
        prod *= x
    print(prod)


if __name__ == "__main__":
    main()
