import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=10)
data = puzzle.input_data

points = [
    [int(x) for x in m]
    for m in re.findall(
        r'position=<((?:-|\W+)\d+),((?:-|\W+)\d+)> velocity=<((?:-|\W+)\d+),((?:-|\W+)\d+)>',
        data)]
boxes = []
for i in range(50_000):
    x, y = zip(*[[x + i * dx, y + i * dy] for x, y, dx, dy in points])
    boxes.append(max(x) - min(x) + max(y) - min(y))

i = np.argmin(boxes)
y, x = zip(*[[x + i * dx, y + i * dy] for x, y, dx, dy in points])
x = np.array(x) - np.min(x)
y = np.array(y) - np.min(y)
d = np.full((np.max(x) + 1, np.max(y) + 1), '.')
d[x, y] = '#'
for row in d:
    print(''.join(row))
puzzle.answer_b = str(i)
