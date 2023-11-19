import re
from collections import Counter
from copy import deepcopy

from aocd.models import Puzzle

puzzle = Puzzle(2022, 6)
data = puzzle.input_data


def first_full(n):
    def lengths():
        starting = Counter(data[:n])
        yield len(+starting)
        for a, b in zip(data, data[n:]):
            starting[a] -= 1
            starting[b] += 1
            yield len(+starting)

    return next(i for i, l in enumerate(lengths(), start=n) if l == n)


puzzle.answer_a = first_full(4)
puzzle.answer_b = first_full(14)
