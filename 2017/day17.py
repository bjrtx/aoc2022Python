from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=17)
data = int(puzzle.input_data)


ring = []
p = 0
for i in range(2017):
    ring.insert(p, i)
    p = (p + data + 1) % (i + 1)

puzzle.answer_a = ring[p]


p = q = 0
for i in range(50_000_000):
    if p == 0:
        q = i
    p = (p + data + 1) % (i + 1)

puzzle.answer_b = q