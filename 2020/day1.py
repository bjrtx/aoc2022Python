import itertools
from collections import defaultdict

from aocd.models import Puzzle
from more_itertools import first

puzzle = Puzzle(year=2020, day=1)
data = [int(x) for x in puzzle.input_data.splitlines()]

d = defaultdict(set)
for i, x in enumerate(data):
    d[x].add(i)

a = first(x for i, x in enumerate(data) if d[2020-x] - {i})
puzzle.answer_a = a * (2020 - a)

b, c = first((x, y) for (i, x), (j, y) in itertools.combinations(enumerate(data), 2) if d[2020 - x - y] - {i, j})
puzzle.answer_b = b * c * (2020 - b - c)