import numpy as np


def main():
    with open("image_data.txt") as f:
        data = np.fromiter(f.read().strip(), int).reshape(-1, 6, 25)
    image = np.ones(data.shape[1:], dtype=int) * 2
    for layer in data:
        image = np.where(image == 2, layer, image)
    print("\n".join("".join(" #"[x] for x in row) for row in image))


if __name__ == "__main__":
    main()
