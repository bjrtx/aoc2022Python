import statistics
from functools import reduce

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
data = puzzle.input_data.splitlines()

syntax_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_points = {'(': 1, '[': 2, '{': 3, '<': 4}
left = {')': '(', ']': '[', '}': '{', '>': '<'}

r_a = 0
val_b = []
for line in data:
    s = []
    for c in line:
        if c in left:
            if s and s[-1] == left[c]:
                s.pop()
            else:
                r_a += syntax_points[c]
                break
        else:
            s.append(c)
    else:
        val_b.append(reduce(lambda p, q: 5 * p + q, (completion_points[c] for c in reversed(s)), 0))


puzzle.answer_a, puzzle.answer_b = r_a, statistics.median(val_b)
