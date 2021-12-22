class Image:
    def __init__(self, algo, in_bounds):
        self.algo = algo
        self.in_bounds = in_bounds
        self.out_of_bounds = 0

    @property
    def bounds(self):
        ymin = min(i for i, _ in self.in_bounds)
        ymax = max(i for i, _ in self.in_bounds)
        xmin = min(j for _, j in self.in_bounds)
        xmax = max(j for _, j in self.in_bounds)
        return ymin, ymax, xmin, xmax

    def iterate(self):
        def get_window_val(i, j):
            val = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    val <<= 1
                    val += self.in_bounds.get((i + di, j + dj), self.out_of_bounds)
            return val
        ymin, ymax, xmin, xmax = self.bounds
        self.in_bounds = {
            (i, j): self.algo[get_window_val(i, j)]
            for i in range(ymin - 1, ymax + 2)
            for j in range(xmin - 1, xmax + 2)
        }
        self.out_of_bounds = self.algo[get_window_val(xmax + 2, ymax + 2)]

    @property
    def pixels_lit(self):
        if self.out_of_bounds:
            return float("inf")
        return sum(self.in_bounds.values())


def main():
    with open("algo_and_image.txt") as f:
        algo_text, image_text = f.read().strip().split("\n\n")
        image = Image(
            [".#".index(char) for char in "".join(algo_text.split("\n"))],
            {
                (i, j): ".#".index(char)
                for i, line in enumerate(image_text.split("\n"))
                for j, char in enumerate(line)
            },
        )

    for _ in range(2):
        image.iterate()
    print(image.pixels_lit)
    for _ in range(50 - 2):
        image.iterate()
    print(image.pixels_lit)


if __name__ == "__main__":
    main()
