import graphlib
import numpy as np

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=6)
data = np.array([list(row) for row in puzzle.input_data.splitlines()])

m, n = len(data), len(data[0])
dirs = [np.array(t) for t in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
([i0], [j0]) = np.where(data == '^')


def seen(data):
    dir_ = 0
    pos = [i0, j0]
    while 0 <= pos[0] < m and 0 <= pos[1] < n:
        yield *pos, dir_
        next_ = dirs[dir_] + pos
        if 0 <= next_[0] < m and 0 <= next_[1] < n and data[*next_] == '#':
            dir_ = (dir_ + 1) % 4
        else:
            pos = next_


s = {(i, j) for (i, j, _) in seen(data)}
puzzle.answer_a = len(s)
res = 0
for pos in s - {(i0, j0)}:
    ddata = data.copy()
    ddata[pos] = '#'
    res += not more_itertools.all_unique(seen(ddata))
puzzle.answer_b = res
