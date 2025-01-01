import itertools
import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=5)
data = puzzle.input_data.splitlines()


def is_nice(s):
    return (
            sum(c in 'aeiou' for c in s) > 2
            and any(a == b for a, b in itertools.pairwise(s))
            and not re.search('ab|cd|pq|xy', s)
    )


def is_nicer(s):
    return bool(re.search(r"(..).*\1", s) and re.search(r"(.).\1", s))


puzzle.answer_a = more_itertools.quantify(data, is_nice)
puzzle.answer_b = more_itertools.quantify(data, is_nicer)
