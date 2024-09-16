import itertools
import re
from collections import Counter, defaultdict
from operator import itemgetter

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=6)
data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".splitlines()
data = puzzle.input_data.splitlines()

points = [[int(x) for x in line.split(',')] for line in data]

print(points)
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
print(drop)
print(grid.transpose())
grid = grid[np.isin(grid, list(drop), invert=True)]
c = np.unique_counts(grid)

puzzle.answer_a = c.counts.max()