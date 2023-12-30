import itertools
from collections import Counter
from functools import cache

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=11)
data = np.array([list(row) for row in puzzle.input_data.splitlines()])
m, n = data.shape


def neighbours(data, p):
    i, j = p
    return [
        data[ii, jj]
        for ii, jj in itertools.product([i - 1, i, i + 1], [j - 1, j, j + 1])
        if (ii, jj) != (i, j) and ii in range(m) and jj in range(n)
    ]


def step(seats):
    nseats = np.copy(seats)
    for i, row in enumerate(seats):
        for j, x in enumerate(row):
            if x == 'L' and '#' not in neighbours(seats, (i, j)):
                nseats[i, j] = '#'
            elif x == '#' and neighbours(seats, (i, j)).count('#') >= 4:
                nseats[i, j] = 'L'
    return nseats


states = more_itertools.iterate(step, data)
final = next(a for a, b in itertools.pairwise(states) if (a == b).all())
puzzle.answer_a = (final == '#').sum()


def nneighbours(data, p):
    i, j = p
    return [
        next((data[ii, jj] for ii, jj in zip(ri, rj) if data[ii, jj] != '.'), None)
        for a, ri in enumerate((range(i - 1, -1, -1), itertools.repeat(i), range(i + 1, m)))
        for b, rj in enumerate((range(j - 1, -1, -1), itertools.repeat(j), range(j + 1, n)))
        if (a, b) != (1, 1)
    ]
def nstep(seats):
    nseats = np.copy(seats)
    for i, row in enumerate(seats):
        for j, x in enumerate(row):
            if x == 'L' and '#' not in nneighbours(seats, (i, j)):
                nseats[i, j] = '#'
            elif x == '#' and nneighbours(seats, (i, j)).count('#') >= 5:
                nseats[i, j] = 'L'
    return nseats


nstates = more_itertools.iterate(nstep, data)
final = next(a for a, b in itertools.pairwise(nstates) if (a == b).all())
puzzle.answer_b = (final == '#').sum()
