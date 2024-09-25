from math import floor, ceil
from statistics import mean

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=6)
data = puzzle.input_data.splitlines()

points = [[int(x) for x in line.split(',')] for line in data]

m = max(p[0] for p in points) + 1
n = max(p[1] for p in points) + 1
grid = np.zeros((m, n), dtype=int)

for i in range(m):
    for j in range(n):
        dists = [abs(i - px) + abs(j - py) for px, py in points]
        m = min(dists)
        best = [i for i, x in enumerate(dists) if x == m]
        if len(best) == 1:
            grid[i, j] = best[0] + 1

drop = set().union(grid[0, :], grid[-1, :], grid[:, 0], grid[:, -1])
grid = grid[np.isin(grid, list(drop), invert=True)]
c = np.unique_counts(grid)

puzzle.answer_a = c.counts.max()

res = 0
x_m, y_m = mean(x for x, _ in points), mean(y for _, y in points)
amplitude = 10_000 / len(points)
puzzle.answer_b = sum(
    sum(abs(x - px) + abs(y - py) for px, py in points) < 10_000
    for x in range(floor(x_m - amplitude), ceil(x_m + amplitude + 1))
    for y in range(floor(y_m - amplitude), ceil(y_m + amplitude + 1))
)
