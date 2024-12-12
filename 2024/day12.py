import itertools
from collections import defaultdict

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=12)
data = np.array([list(line) for line in puzzle.input_data.splitlines()])

regions = np.zeros_like(data, dtype=int)
m, n = data.shape
perimeters = defaultdict(int)
areas = defaultdict(int)
corners = defaultdict(int)


def colour(i, j, col):
    regions[i, j] = col
    areas[col] += 1

    neighbours = [
        (i + di, j + dj)
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1])
        if 0 <= i + di < m and 0 <= j + dj < n and data[i + di, j + dj] == data[i, j]
    ]

    perimeters[col] += 4 - len(neighbours)

    # Use corners to detect sides
    for dirs in (([-1, 0], [0, 1]), ([-1, 0], [0, -1]), ([1, 0], [0, 1]), ([1, 0], [0, -1])):
        if not any(0 <= i + ii < m and 0 <= j + jj < n and data[i + ii, j + jj] == data[i, j] for ii, jj in dirs):
            corners[col] += 1
        elif all(0 <= i + ii < m and 0 <= j + jj < n and data[i + ii, j + jj] == data[i, j] for ii, jj in dirs):
            (a, b), (c, d) = dirs
            corners[col] += data[i + a + c, j + b + d] != data[i, j]

    for ii, jj in neighbours:
        if not regions[ii, jj]:
            colour(ii, jj, col)


cols = itertools.count(1)
for i in range(m):
    for j in range(n):
        if not regions[i, j]:
            colour(i, j, next(cols))

puzzle.answer_a, puzzle.answer_b = (sum(areas[c] * v[c] for c in areas) for v in (perimeters, corners))
