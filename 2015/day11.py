import re

from more_itertools import iterate, take, triplewise
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=11)
data = puzzle.input_data.strip()


def next_string(s):
    if s.endswith('z'):
        return next_string(s[:-1]) + 'a'
    else:
        return s[:-1] + chr(ord(s[-1] if s else 'a') + 1)


def is_valid(s):
    return (
            any(
                a == b - 1 == c - 2 for a, b, c in triplewise(map(ord, s))
            )
            and not re.search('[iol]', s)
            and re.search(r"(.)\1.*(.)\2", s) is not None
    )


puzzle.answer_a, puzzle.answer_b = take(2, filter(is_valid, iterate(next_string, data)))
