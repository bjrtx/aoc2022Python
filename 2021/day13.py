import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=13)
data = puzzle.input_data

points, folds = data.split('\n\n')
points = {eval(line) for line in points.splitlines()}
folds = ((d, int(p)) for d, p in re.findall(r'fold along ([xy])=(\d+)', folds))


def fold(dir_, pos):
    global points
    if dir_ == 'x':
        points = {(min(x, 2 * pos - x), y) for x, y in points}
    else:
        points = {(x, y if y <= pos else 2 * pos - y) for x, y in points}


first, *others = folds
fold(*first)
puzzle.answer_a = len(points)
for f in others:
    fold(*f)
y, x = zip(*points)
d = np.full((max(x) + 1, max(y) + 1), '.')
d[x, y] = '#'
for row in d:
    print(''.join(row))
