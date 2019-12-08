import matplotlib.pyplot as plt
import numpy as np


def main():
    with open("image_data.txt") as f:
        data = np.fromiter(f.read().strip(), np.int8).reshape(-1, 6, 25)
    image = np.ones(data.shape[1:]) * 2
    for layer in data:
        image = np.where(image == 2, layer, image)
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    main()
