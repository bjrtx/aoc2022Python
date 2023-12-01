import itertools
import operator
import re
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=10)
data = puzzle.input_data.strip()


def look_and_say(s):
    for k, g in itertools.groupby(s):
        yield sum(1 for _ in g)
        yield int(k)


s = data
for i in range(40):
    s = look_and_say(s)

puzzle.answer_a = sum(1 for _ in s)

s = data
for i in range(50):
    s = look_and_say(s)

puzzle.answer_b = sum(1 for _ in s)