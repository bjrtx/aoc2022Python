import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=5)
data = [int(x) for x in puzzle.input_data.splitlines()]

jumps = data[:]
index = 0
for step in itertools.count(1):
    j = jumps[index]
    jumps[index] += 1
    index += j
    if index < 0 or index >= len(jumps):
        break

# noinspection PyUnboundLocalVariable
puzzle.answer_a = step

jumps = data[:]
index = 0
for step in itertools.count(1):
    j = jumps[index]
    jumps[index] += - 1 if j >= 3 else 1
    index += j
    if index < 0 or index >= len(jumps):
        break

puzzle.answer_b = step
