import operator

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=6)
answers = list(more_itertools.split_at(puzzle.input_data.splitlines(), pred=operator.not_))

puzzle.answer_a = sum(len(set().union(*a)) for a in answers)
puzzle.answer_b = sum(len(set(a[0]).intersection(*a)) for a in answers)
