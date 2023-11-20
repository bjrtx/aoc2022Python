import itertools
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=5)
data = puzzle.input_data.splitlines()


def is_nice(s):
    return (
            sum(c in 'aeiou' for c in s) > 2
            and any(a == b for a, b in itertools.pairwise(s))
            and all(sub not in s for sub in ('ab', 'cd', 'pq', 'xy'))
    )


def is_nicer(s):
    return bool(re.search(r"(..).*\1", s) and re.search(r"(.).\1", s))


puzzle.answer_a = sum(is_nice(s) for s in data)
puzzle.answer_b = sum(is_nicer(s) for s in data)