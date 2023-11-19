import itertools
from functools import cmp_to_key

import networkx as nx

from aocd.models import Puzzle

puzzle = Puzzle(2022, 13)
data = puzzle.input_data

lines = data.splitlines()
pairs = [(eval(a), eval(b)) for a, b in zip(lines[::3], lines[1::3])]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else -1 if right < left else 0
    else:
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        for c in itertools.starmap(compare, zip(left, right)):
            if c != 0:
                return c
        else:
            return compare(len(left), len(right))


puzzle.answer_a = sum(i for i, (a, b) in enumerate(pairs, start=1) if compare(a, b) == 1)

dividers = ([[2]], [[6]])
all_packets = list(itertools.chain.from_iterable(pairs)) + list(dividers)
indices = [sum(compare(p, d) == 1 for p in all_packets) + 1 for d in dividers]
puzzle.answer_b = indices[0] * indices[1]