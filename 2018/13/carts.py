from collections import namedtuple


class Cart:
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction
        self.n_turns = 0
        self.crashed = False


def add_tup(t1, t2):
    return tuple(a + b for a, b in zip(t1, t2))


def main():
    with open("tracks.txt") as f:
        tracks = [list(line[:-1]) for line in f]

    direction_map = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    carts = []
    for i in range(len(tracks)):
        for j in range(len(tracks[0])):
            char = tracks[i][j]
            if char in direction_map:
                cart = Cart((i, j), direction_map[char])
                carts.append(cart)
                tracks[i][j] = "|" if cart.direction[0] else "-"

    turn_map = {0: lambda t: (-t[1], t[0]), 1: lambda t: t, 2: lambda t: (t[1], -t[0])}
    no_crashes = True
    while True:
        carts.sort(key=lambda c: c.location)
        for cart in carts:
            if cart.crashed:
                continue
            # Update location
            cart.location = add_tup(cart.location, cart.direction)
            # Change direction if needed
            char = tracks[cart.location[0]][cart.location[1]]
            if char == "/":
                cart.direction = (-cart.direction[1], -cart.direction[0])
            elif char == "\\":
                cart.direction = (cart.direction[1], cart.direction[0])
            elif char == "+":
                cart.direction = turn_map[cart.n_turns](cart.direction)
                cart.n_turns = (cart.n_turns + 1) % 3
            # Check for a crash
            for other_cart in carts:
                if (
                    not other_cart.crashed
                    and other_cart is not cart
                    and cart.location == other_cart.location
                ):
                    if no_crashes:
                        y, x = cart.location
                        print(x, y, sep=",")
                        no_crashes = False
                    cart.crashed = other_cart.crashed = True
        carts = [cart for cart in carts if not cart.crashed]
        if len(carts) == 1:
            y, x = carts[0].location
            print(x, y, sep=",")
            return


if __name__ == "__main__":
    main()
