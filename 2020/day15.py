import itertools
from collections import defaultdict

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=15)

data = eval(puzzle.input_data)


def game():
    seen = defaultdict(tuple)
    for i, x in enumerate(data):
        seen[x] = (l[-1], i) if (l := seen[x]) else (i,)
        yield x
    for step in itertools.count(len(data)):
        x = (l[-1] - l[-2]) if len((l := seen[x])) >= 2 else 0
        seen[x] = (l[-1], step) if (l := seen[x]) else (step,)
        yield x


puzzle.answer_a = more_itertools.nth(game(), 2019)
# slow, ca. 20 s
puzzle.answer_b = more_itertools.nth(game(), 29_999_999)
