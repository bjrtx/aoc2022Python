import itertools

from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2024, day=2)
data = [
    [int(x) for x in line.split()]
    for line in puzzle.input_data.splitlines()]


def aux(vals, dampener):
    diffs = [b - a for a, b in itertools.pairwise(vals)]
    fails = [i for i, x in enumerate(diffs) if x not in {1, 2, 3}]
    return (not fails
            or dampener and len(fails) <= 2 and any(
                aux(vals[:j] + vals[j + 1:], dampener=False)
                for f in fails
                for j in (f, f + 1)
            ))


def is_safe(vals, dampener):
    return aux(vals, dampener) or aux([-v for v in vals], dampener)


puzzle.answer_a = sum(is_safe(r, False) for r in data)
puzzle.answer_b = sum(is_safe(r, True) for r in data)
