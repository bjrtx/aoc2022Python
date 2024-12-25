from itertools import product

from more_itertools import partition
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=25)
data = puzzle.input_data


schematics = (np.array([list(row) for row in block.splitlines()]) == '#' for block in data.split('\n\n'))
keys, locks = partition(lambda s: s[0].all(), schematics)
keys = (np.sum(s, axis=0) - 1 for s in keys)
locks = (np.sum(s, axis=0) - 1 for s in locks)

puzzle.answer_a = str(sum((key + lock <= 5).all() for key, lock in product(keys, locks)))
