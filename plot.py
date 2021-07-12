import matplotlib.pyplot as plt
import sys
from utils import get_strokes, keyboard_map

# make graph look better
plt.axis("equal")
plt.axis("off")

# create keyboard map
key_xs = list(map(lambda x: x[0], list(keyboard_map.values())))
key_ys = list(map(lambda x: x[1], list(keyboard_map.values())))
plt.scatter(key_xs, key_ys, s=1, c="black")

# generate letters
marked = {}

for i, word in enumerate(sys.argv[1:]):
    response = list(get_strokes(word))
    xs = list(map(lambda x: x[1][0], response))
    ys = list(map(lambda x: x[1][1], response))

    plt.annotate(word, (200, 20 * i), weight="bold")

    for i, (c, (x, y)) in enumerate(response):
        plt.annotate(
            c,
            (x, y),
            textcoords="offset points",
            xytext=(5, 5) if ((x, y) not in marked or marked[(x, y)] == c) else (-5, 5),
            ha="center",
            weight="bold" if i == 0 else "normal",
        )
        marked[(x, y)] = marked.get((x, y), c)

    plt.plot(xs, ys, [".r-", ".g-", ".b-"][i % 3])

plt.show()
