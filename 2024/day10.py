import functools
import itertools
from collections import Counter

import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=10)
data = puzzle.input_data.splitlines()
data = np.array([[int(d) for d in line] for line in data])
m, n = data.shape

dirs = ([-1, 0], [1, 0], [0, -1], [0, 1])
zeroes = np.argwhere(data == 0)
res = 0
for p in zeroes:
    boundary = [p]
    for i in range(1, 10):
        boundary = (np.array(pos) + delta for pos in boundary for delta in dirs)
        boundary = {
            tuple(pos)
            for pos in boundary
            if 0 <= pos[0] < m and 0 <= pos[1] < n and data[*pos] == i}
    res += len(boundary)
puzzle.answer_a = res

boundary = [(p, 1) for p in zeroes]
for i in range(1, 10):
    boundary = ((np.array(pos) + delta, mult) for pos, mult in boundary for delta in dirs)
    boundary = [
        (tuple(pos), mult)
        for pos, mult in boundary
        if 0 <= pos[0] < m and 0 <= pos[1] < n and data[*pos] == i]
    d = Counter()
    for pos, mult in boundary:
        d[pos] += mult
    boundary = d.items()
puzzle.answer_b = sum(v for _, v in boundary)
