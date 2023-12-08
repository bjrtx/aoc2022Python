import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=2)
data = [[int(x) for x in line.split()] for line in puzzle.input_data.splitlines()]

puzzle.answer_a = sum(max(l) - min(l) for l in data)

divs = [[divmod(b, a) for a, b in itertools.combinations(sorted(line), 2)] for line in data]
puzzle.answer_b = sum(next(q for q, r in d if r == 0) for d in divs)
