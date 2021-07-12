from shapely.geometry import LineString, point, linestring
from utils import get_strokes
import sys


def find_intersections(word):
    response = list(get_strokes(word))
    ignore_points = list(map(lambda x: tuple(x[1]), list(response)))
    lines = []
    int_count = 0

    # does going back to an old letter count as an intersection?
    if len(set(ignore_points)) != len(ignore_points):
        return float("inf")

    for i in range(len(response) - 1):
        l = LineString([response[i][1], response[i + 1][1]])

        # do duplicated letters count as an intersection?
        if l.length == 0.0:
            return float("inf")

        for line in lines:
            intersection = line.intersection(l)
            if (
                (type(intersection) is not point.Point)
                or (intersection.coords[0] not in ignore_points)
            ) and intersection:
                if type(intersection) is linestring.LineString:
                    return float("inf")
                int_count += 1
        lines.append(l)
    return int_count


for word in sys.argv[1:]:
    print(f"{word}: {find_intersections(word)}")
