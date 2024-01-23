import itertools

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=1)
data = [eval(x) for x in puzzle.input_data.splitlines()]

puzzle.answer_a = sum(data)
puzzle.answer_b = next(more_itertools.duplicates_everseen(
    itertools.accumulate(itertools.cycle(data), initial=0)
))
