import itertools
import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=20)
data = puzzle.input_data.splitlines()

particles = np.array([
    list(itertools.batched(map(int, re.findall(r'-?\d+', line)), 3))
    for line in data
])
# Lucky input
puzzle.answer_a = int(np.linalg.norm(particles[:, 2], ord=1, axis=1).argmin())
