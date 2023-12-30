import itertools
from collections import Counter
from functools import cache
from math import prod

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=13)
timestamp, ids = puzzle.input_data.splitlines()
timestamp = int(timestamp)
ids = ids.split(',')  # all prime numbers, how curious


def delay(bus):
    r = timestamp % bus
    return bus - r if r else 0


delay, bus = min((delay(b), b) for b in (int(x) for x in ids if x != 'x'))
puzzle.answer_a = delay * bus

constraints = [(-i, int(b)) for (i, b) in enumerate(ids) if b != 'x']
"""sage
e = crt_basis([b for _, b in constraints])
n = sum(i * v for (i,_), v in zip(constraints, e))
n % prod(b for _, b in constraints)
"""