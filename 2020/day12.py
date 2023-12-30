import itertools
from collections import Counter
from functools import cache

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=12)
data = puzzle.input_data.splitlines()

pos = np.zeros(2, dtype=np.int32)
dir = np.array([0, 1], dtype=np.int32)

for line in data:
    match [line[0], int(line[1:])]:
        case ['N', v]:
            pos[0] += v
        case ['S', v]:
            pos[0] -= v
        case ['E', v]:
            pos[1] += v
        case ['W', v]:
            pos[1] -= v
        case [('L' | 'R') as direction, v]:
            match ((1 if direction == 'L' else -1) * v) % 360:
                case 90:
                    dir[:] = [dir[1], -dir[0]]
                case 180:
                    dir *= -1
                case 270:
                    dir[:] = [-dir[1], dir[0]]
        case ['F', v]:
            pos += dir * v

puzzle.answer_a = abs(pos).sum()

pos = np.zeros(2, dtype=np.int32)
dir = np.array([1, 10], dtype=np.int32)

for line in data:
    match [line[0], int(line[1:])]:
        case ['N', v]:
            dir[0] += v
        case ['S', v]:
            dir[0] -= v
        case ['E', v]:
            dir[1] += v
        case ['W', v]:
            dir[1] -= v
        case [('L' | 'R') as direction, v]:
            match ((1 if direction == 'L' else -1) * v) % 360:
                case 90:
                    dir[:] = [dir[1], -dir[0]]
                case 180:
                    dir *= -1
                case 270:
                    dir[:] = [-dir[1], dir[0]]
        case ['F', v]:
            pos += dir * v

puzzle.answer_b = abs(pos).sum()
