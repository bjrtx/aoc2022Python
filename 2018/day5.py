import itertools
import re
from collections import Counter, defaultdict
from operator import itemgetter

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=5)
data = puzzle.input_data


def react(string, skip=None):
    s = []
    for c in string:
        if c.lower() != skip:
            if s and s[-1].lower() == c.lower() and s[-1] != c:
                s.pop()
            else:
                s.append(c)
    return len(s)


puzzle.answer_a = react(data)
puzzle.answer_b = min(react(data, skip) for skip in set(data))
