import itertools
import math
from collections import defaultdict

import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=8)
data = np.array([list(line) for line in puzzle.input_data.splitlines()])

m, n = data.shape

locations = defaultdict(list)
for idx in np.argwhere(data != '.'):
    locations[data[*idx]].append(idx)
unique_locations = {
    tuple(2 * q - p)
    for v in locations.values()
    for p, q in itertools.permutations(v, 2)
}
puzzle.answer_a = sum(0 <= x < m and 0 <= y < n for x, y in unique_locations)

unique_locations = set()
for v in locations.values():
    for p, q in itertools.permutations(v, 2):
        delta = q - p
        delta //= math.gcd(*delta)
        for i in range(max(m, n)):
            unique_locations.add(tuple(p + i * delta))
            unique_locations.add(tuple(p - i * delta))
puzzle.answer_b = sum(0 <= x < m and 0 <= y < n for x, y in unique_locations)
