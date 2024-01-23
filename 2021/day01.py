import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)
data = puzzle.input_data.splitlines()
data = [int(line) for line in data]

puzzle.answer_a = sum(b > a for a, b in itertools.pairwise(data))
puzzle.answer_b = sum(b > a for a, b in zip(data, data[3:]))
