import graphlib
import re

import more_itertools
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=7)
data = [[int(x) for x in re.split(r': |\W+', line)] for line in puzzle.input_data.splitlines()]


def reaches(list_, target, extend=False):
    v0, *t = list_
    values = {v0}
    for x in t:
        if extend:
            values = {x + v for v in values} | {x * v for v in values} | {int(str(v)+str(x)) for v in values}
        else:
            values = {x + v for v in values} | {x * v for v in values}
    return target in values


puzzle.answer_a = sum(
    target * reaches(rhs, target, False)
    for (target, *rhs) in data
)
puzzle.answer_b = sum(
    target * reaches(rhs, target, True)
    for (target, *rhs) in data
)
