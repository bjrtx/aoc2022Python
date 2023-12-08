import itertools

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=1)
data = puzzle.input_data.strip()

puzzle.answer_a = 2 * data.count('(') - len(data)

positions = itertools.accumulate(1 if c == '(' else -1 for c in data)
puzzle.answer_b = next(more_itertools.iter_index(positions, -1)) + 1
