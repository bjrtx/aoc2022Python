import re

from aocd.models import Puzzle

puzzle = Puzzle(2022, 4)
data = puzzle.input_data.splitlines()

integers = [[int(x) for x in re.split(r"[,-]", line)] for line in data]

puzzle.answer_a = sum(bool(a <= c <= d <= b or c <= a <= b <= d) for a, b, c, d in integers)
puzzle.answer_b = sum(bool(not(b < c or d < a)) for a, b, c, d in integers)
