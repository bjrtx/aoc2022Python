import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=1)
data = [int(c) for c in puzzle.input_data]

puzzle.answer_a = sum(a for a, b in itertools.pairwise(data) if a == b) + data[0] * (data[0] == data[-1])

n = len(data) // 2
shifted = itertools.chain(data[n:], data[:n])
puzzle.answer_b = sum(a for a, b in zip(data, shifted) if a == b)
