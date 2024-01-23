from statistics import mean, median
from math import ceil, floor

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=7)
data = eval(puzzle.input_data)

m = int(median(data))
puzzle.answer_a = sum(abs(x - m) for x in data)

mean = mean(data)
puzzle.answer_b = min(sum(abs(x - m) * (abs(x - m) + 1) // 2 for x in data) for m in (ceil(mean), floor(mean)))
