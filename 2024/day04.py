import itertools

from aocd.models import Puzzle
import numpy as np


puzzle = Puzzle(year=2024, day=4)
data = np.array([list(row) for row in puzzle.input_data.splitlines()])
m, n = data.shape
dirs = itertools.chain(
    data,
    data.T,
    (data.diagonal(i) for i in range(-m, n)),
    (np.flipud(data).diagonal(i) for i in range(-n, m))
)
strings = (''.join(r) for r in dirs)
puzzle.answer_a = sum(s.count('XMAS') + s.count('SAMX') for s in strings)

mats = (data[i:i + 3, j:j + 3] for i in range(m - 2) for j in range(n - 2))
puzzle.answer_b = sum(
    p[1, 1] == 'A' and any(
        m[0, 0] == m[2, 0] == 'M' and m[0, 2] == m[2, 2] == 'S'
        for m in (p, np.fliplr(p), np.flipud(p), np.rot90(p), np.rot90(p, k=-1))
    )
    for p in mats
)
