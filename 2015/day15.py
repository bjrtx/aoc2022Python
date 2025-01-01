import itertools
import math
import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=15)
data = puzzle.input_data.splitlines()

ingredients = np.array([[int(m[0]) for m in re.finditer(r'-?\d+', line)] for line in data])


def simplex(n):
    for p in itertools.product(range(101), repeat=n-1):
        s = 100 - sum(p)
        if s >= 0:
            yield *p, s


def scores(count_calories):
    ingredients_no_calories = ingredients[:, :-1]
    calories = ingredients[:, -1] if count_calories else None
    for p in simplex(len(ingredients_no_calories)):
        if not count_calories or np.dot(p, calories) == 500:
            total = np.maximum(p @ ingredients_no_calories, 0)
            yield math.prod(total)


puzzle.answer_a = max(scores(count_calories=False))
puzzle.answer_b = max(scores(count_calories=True))
