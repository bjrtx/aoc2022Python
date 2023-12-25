import functools
import itertools

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=18)
data = np.array([[c == '#' for c in row] for row in puzzle.input_data.splitlines()])
m, n = data.shape


def neighbours(pos):
    i, j = pos
    return (
        (i + di, j + dj)
        for di, dj in itertools.product(range(-1, 2), repeat=2)
        if (di or dj) and i + di in range(m) and j + dj in range(n)
    )


corners = tuple(itertools.product((0, m - 1), (0, n - 1)))


def conway_step(data: np.ndarray, second=False):
    ndata = np.zeros_like(data)
    for pos in itertools.product(range(m), range(n)):
        count = sum(data[nb] for nb in neighbours(pos))
        ndata[pos] = (second and pos in corners) or count == 3 or (count == 2 and data[pos])
    return ndata


# Somewhat too slow (ca. 1 min.)
puzzle.answer_a, puzzle.answer_b = [
    more_itertools.nth(more_itertools.iterate(f, data), 100).sum()
    for f in (conway_step, functools.partial(conway_step, second=True))
]
