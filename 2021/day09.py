from collections import Counter
from functools import cache
from math import prod

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=9)
data = puzzle.input_data.splitlines()

heatmap = np.array(
    [
        [int(c) for c in row]
        for row in data
    ]
)


@cache
def basin(i, j):
    neighbours = [
        (a, b)
        for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        if a in range(len(heatmap)) and b in range(len(heatmap[0]))
    ]
    if heatmap[i, j] == 9:
        return i, j
    for a, b in neighbours:
        if heatmap[a, b] < heatmap[i, j]:
            return basin(a, b)
    else:
        return i, j


def low_points():
    for i, row in enumerate(heatmap):
        for j, x in enumerate(row):
            if basin(i, j) == (i, j) and x != 9:
                yield x


puzzle.answer_a = sum(1 + x for x in low_points())
basins = Counter(basin(i, j) for i in range(len(heatmap)) for j in range(len(heatmap[0])))
puzzle.answer_b = prod(n for _, n in basins.most_common(3))
