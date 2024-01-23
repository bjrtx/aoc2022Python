import itertools
from collections import Counter

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=2)
data = puzzle.input_data.splitlines()

counts = [Counter(w).values() for w in data]

print(sum(2 in c for c in counts) * sum(3 in c for c in counts))
puzzle.answer_a = sum(2 in c for c in counts) * sum(3 in c for c in counts)

p = next(
    p
    for p in itertools.combinations(data, 2)
    if more_itertools.exactly_n(zip(*p), 1, predicate=lambda p: p[0] != p[1])
)
puzzle.answer_b = ''.join(x for x, y in zip(*p) if x == y)
