import collections
import itertools
import re
from functools import cache

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=9)
data = puzzle.input_data

cancelled = garbage = False
group_scores = 0
score = 0
garbage_length = 0
for c in data:
    if cancelled:
        cancelled = False
        continue
    elif c == '!':
        cancelled = True
        continue
    elif garbage:
        garbage = c != '>'
        garbage_length += garbage
        continue
    match c:
        case '<':
            garbage = True
        case '{':
            group_scores += 1
            score += group_scores
        case '}':
            group_scores -= 1

puzzle.answer_a, puzzle.answer_b = score, garbage_length
