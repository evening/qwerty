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
response = list(get_strokes(sys.argv[1]))
xs = list(map(lambda x: x[1][0], response))
ys = list(map(lambda x: x[1][1], response))

plt.annotate(sys.argv[1], (200, 0), weight="bold")

marked = {}
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

plt.plot(xs, ys, ".r-")
plt.show()
