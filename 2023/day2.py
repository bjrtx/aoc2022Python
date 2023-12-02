import functools
import math
import operator
from collections import Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)
data = puzzle.input_data.splitlines()

outcomes = [[] for _ in data]

for i, line in enumerate(data):
    _, line = line.split(":", 2)
    for draw in line.split(";"):
        counts = Counter()
        for part in draw.split(","):
            n, col = part.split()
            counts[col] = int(n)
        outcomes[i].append(counts)

maxima = [functools.reduce(operator.or_, c) for c in outcomes]

puzzle.answer_a = sum(
    i for i, c in enumerate(maxima, start=1)
    if c <= Counter(red=12, green=13, blue=14)
)

puzzle.answer_b = sum(math.prod(c.values()) for c in maxima)
