from collections import namedtuple
from itertools import chain, product
from functools import partial
import re


Point = namedtuple("Point", "x y z")


class Cube:
    def __init__(self, point, side_len):
        self.point = point
        self.side_len = side_len
        self.vertices = self._get_vertices()
        self.centre = self._get_centre()

    def __contains__(self, item):
        return all(sx <= ix < sx + self.side_len for sx, ix in zip(self.point, item))

    def __repr__(self):
        return f"Cube({self.point}, {self.side_len})"

    def _get_centre(self):
        x, y, z = self.point
        half_side_len = self.side_len // 2
        return Point(x + half_side_len, y + half_side_len, z + half_side_len)

    def _get_vertices(self):
        x, y, z = self.point
        return [
            Point(x + dx, y + dy, z + dz)
            for dx, dy, dz in product((0, self.side_len), repeat=3)
        ]

    @property
    def subcubes(self):
        x, y, z = self.point
        new_side_len = self.side_len // 2
        for dx, dy, dz in product((0, new_side_len), repeat=3):
            yield Cube(Point(x + dx, y + dy, z + dz), new_side_len)


def dist(point1, point2):
    """Manhattan distance between two points"""
    return sum(abs(x1 - x2) for x1, x2 in zip(point1, point2))


class Octahedron:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius
        self.vertices = self._get_vertices()

    def __contains__(self, item):
        return dist(self.point, item) <= self.radius

    def __repr__(self):
        return f"Octahedron({self.point}, {self.radius})"

    def _get_vertices(self):
        x, y, z = self.point
        vertices = []
        for d in (-self.radius, self.radius):
            vertices.extend((
                Point(x + d, y, z),
                Point(x, y + d, z),
                Point(x, y, z + d),
            ))
        return vertices


def get_bounding_cube(nanobots):
    """Get cube guaranteed to contain the point we are seeking"""
    max_dim = (
        max(chain.from_iterable(map(abs, bot.point) for bot in nanobots))
        + max(bot.radius for bot in nanobots)
    )
    dim = 1
    while dim < max_dim:
        dim *= 2
    return Cube(Point(-dim, -dim, -dim), 2 * dim)


def intersect(cube, octahedron):
    """
    Test for intersection of cube and octahedron by checking if at least one
    vertex or the centre one shape is contained in the other.
    """
    return (
        cube.centre in octahedron
        or any(vertex in octahedron for vertex in cube.vertices)
        or octahedron.point in cube
        or any(vertex in cube for vertex in octahedron.vertices)
    )


def find_central_point(nanobots):
    max_in_range = 0
    q = [(get_bounding_cube(nanobots), nanobots)]
    while q:
        cube, nanobots = q.pop()
        if len(nanobots) > max_in_range:
            if cube.side_len == 1:
                n_in_range = sum(cube.point in nanobot for nanobot in nanobots)
                if n_in_range > max_in_range:
                    max_in_range = n_in_range
                    central_point = cube.point
            else:
                q.extend(
                    (subcube, tuple(filter(partial(intersect, subcube), nanobots)))
                    for subcube in cube.subcubes
                )
    return central_point


def main():
    nanobots = []
    with open("nanobots.txt") as f:
        for line in f:
            x, y, z, r = map(int, re.findall(r"-?\d+", line))
            nanobots.append(Octahedron(Point(x, y, z), r))
    print(sum(find_central_point(nanobots)))


if __name__ == "__main__":
    main()
