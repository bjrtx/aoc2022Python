import re

import more_itertools
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
                a == b - 1 == c - 2 for a, b, c in more_itertools.triplewise(map(ord, s))
            )
            and all(c not in s for c in 'iol')
            and re.search(r"(.)\1.*(.)\2", s) is not None
    )


passwd = data
while not is_valid(passwd):
    passwd = next_string(passwd)

puzzle.answer_a = passwd
passwd = next_string(passwd)
while not is_valid(passwd):
    passwd = next_string(passwd)
puzzle.answer_b = passwd
