from collections import Counter, deque, namedtuple
from enum import Enum


Pulse = Enum("Pulse", ("LOW", "HIGH"))
Event = namedtuple("Event", ("source", "dest", "pulse"))
ModuleSpec = namedtuple("ModuleSpec", ("type", "name", "destinations"))


def broadcaster(_, __, destinations):
    def process(event):
        return [Event("broadcaster", dest, event.pulse) for dest in destinations]
    return process


def flipflop(name, _, destinations):
    active = False
    def process(event):
        if event.pulse is Pulse.HIGH:
            return []
        nonlocal active
        pulse = Pulse.LOW if active else Pulse.HIGH
        active = not active
        return [Event(name, dest, pulse) for dest in destinations]
    return process


def conjuction(name, inputs, destinations):
    last_pulse = {inp: Pulse.LOW for inp in inputs}
    def process(event):
        last_pulse[event.source] = event.pulse
        pulse = (
            Pulse.LOW
            if all(pulse is Pulse.HIGH for pulse in last_pulse.values())
            else Pulse.HIGH
        )
        return [Event(name, dest, pulse) for dest in destinations]
    return process


def parse(module_spec_str):
    name, destinations = module_spec_str.strip().split(" -> ")
    destinations = destinations.split(", ")
    if name == "broadcaster":
        return ModuleSpec(broadcaster, "broadcaster", destinations)
    elif name.startswith("%"):
        return ModuleSpec(flipflop, name[1:], destinations)
    elif name.startswith("&"):
        return ModuleSpec(conjuction, name[1:], destinations)


def main():
    with open("module_config.txt") as f:
        module_specs = [parse(line.strip()) for line in f]
    modules = {}
    for module_spec in module_specs:
        inputs = [
            spec.name
            for spec in module_specs
            if module_spec.name in spec.destinations
        ]
        modules[module_spec.name] = module_spec.type(
            module_spec.name, inputs, module_spec.destinations
        )

    event_queue = deque()

    def push_button():
        event_queue.append(Event("button", "broadcaster", Pulse.LOW))

    outputs = Counter()
    for _ in range(1000):
        push_button()
        while event_queue:
            event = event_queue.popleft()
            outputs[event.pulse] += 1
            if event.dest in modules:
                event_queue.extend(modules[event.dest](event))
    print(outputs[Pulse.LOW] * outputs[Pulse.HIGH])


if __name__ == "__main__":
    main()
