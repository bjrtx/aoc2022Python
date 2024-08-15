import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=11)
data = puzzle.input_data

pos = np.zeros(2)
m = dist = 0
d = {
    k: np.array(v)
    for k, v in {'nw': [-1, 1], 'n': [0, 2], 'ne': [1, 1], 'se': [1, -1],
                 's': [0, -2], 'sw': [-1, -1]}.items()
}
for direction in data.split(','):
    pos += d[direction]
    dist = int(np.abs(pos).sum()) // 2
    m = max(m, dist)

puzzle.answer_a, puzzle.answer_b = dist, m
