import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=3)
data = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2""".splitlines()
data = puzzle.input_data.splitlines()


rectangles = []
for line in data:
    m = re.fullmatch(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    rectangles.append([int(x) for x in m.groups()])

m = max(r[1] + r[3] for r in rectangles) + 1
n = max(r[2] + r[4] for r in rectangles) + 1
fabric = np.zeros((m, n))
for _, a, b, w, h in rectangles:
    fabric[a: a + w, b: b + h] += 1

puzzle.answer_a = np.sum(fabric > 1)

puzzle.answer_b = next(
    id_
    for id_, a, b, w, h in rectangles
    if np.all(fabric[a: a + w, b: b + h] == 1)
)

