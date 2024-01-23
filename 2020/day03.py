import itertools
import math
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)
data = puzzle.input_data.splitlines()


def tree_count(a, b):
    return sum(
        data[i][j % len(data[0])] == '#'
        for i, j in zip(range(0, len(data), b), itertools.count(0, a))
    )


puzzle.answer_a = tree_count(3, 1)
puzzle.answer_b = math.prod(tree_count(*p) for p in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))