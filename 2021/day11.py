import itertools

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=11)
data = puzzle.input_data.splitlines()

energy_levels = np.array([[int(c) for c in row] for row in data])
m, n = energy_levels.shape


def neighbours(i, j):
    for ii, jj in itertools.product(range(i - 1, i + 2), range(j - 1, j + 2)):
        if 0 <= ii < m and 0 <= jj < n and (ii, jj) != (i, j):
            yield ii, jj


flashes = 0
for step in itertools.count(1):
    energy_levels += 1
    flashing = {tuple(pos) for pos in np.argwhere(energy_levels > 9)}
    flashed = set()
    while flashing:
        i, j = flashing.pop()
        for x, y in neighbours(i, j):
            energy_levels[x, y] += 1
            if (x, y) not in flashed and energy_levels[x, y] > 9:
                flashing.add((x, y))
        flashed.add((i, j))
    flashes += len(flashed)
    energy_levels = np.where(energy_levels < 10, energy_levels, 0)
    if step == 100:
        puzzle.answer_a = flashes
    if len(flashed) == m * n:
        puzzle.answer_b = step
        break
