import functools
import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=9)
data = puzzle.input_data.splitlines()

data = [[int(x) for x in line.split()] for line in data]


total_a = total_b = 0
for line in data:
    diffs = line[:]
    first = [diffs[0]]
    while any(diffs):
        total_a += diffs[-1]
        diffs = [b - a for a, b in itertools.pairwise(diffs)]
        first.append(diffs[0])
    total_b += functools.reduce(lambda a, b: b - a, reversed(first))

puzzle.answer_a = total_a
puzzle.answer_b = total_b
