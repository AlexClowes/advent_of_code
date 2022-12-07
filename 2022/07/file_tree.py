from collections import namedtuple
from enum import Enum


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.parent = parent

    def add_child(self, child):
        assert child.name not in self.children
        self.children[child.name] = child

    def get_child(self, child_name):
        return self.children[child_name]

    @property
    def size(self):
        return sum(child.size for child in self.children.values())

    def walk(self):
        yield self
        for child in self.children.values():
            if isinstance(child, Directory):
                yield from child.walk()


File = namedtuple("File", ("name", "size"))


def build_tree(terminal_output):
    assert next(terminal_output) == ["$", "cd", "/"]
    current_loc = root = Directory("/")

    for line in terminal_output:
        match line:
            case "$", "cd", "..":
                current_loc = current_loc.parent
            case "$", "cd", dirname:
                current_loc = current_loc.get_child(dirname)
            case "$", "ls":
                pass
            case "dir", name:
                current_loc.add_child(Directory(name, parent=current_loc))
            case size, name:
                current_loc.add_child(File(name, int(size)))

    return root


def main():
    with open("terminal_output.txt") as f:
        tree = build_tree(line.strip().split() for line in f)

    print(sum(node.size for node in tree.walk() if node.size < 100000))

    space_available = 70000000
    space_required = 30000000
    space_used = tree.size
    need_to_free = space_used + space_required - space_available
    print(min(node.size for node in tree.walk() if node.size >= need_to_free))


if __name__ == "__main__":
    main()
