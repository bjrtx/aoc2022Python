from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2024, day=1)
data = puzzle.input_data.splitlines()

a, b = zip(*((int(x) for x in line.split()) for line in data))
c = Counter(b)
puzzle.answer_a = sum(abs(x - y) for x, y in zip(sorted(a), sorted(b)))
puzzle.answer_b = sum(x * c[x] for x in a)

