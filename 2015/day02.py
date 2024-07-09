from itertools import combinations

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=2)
data = [sorted(int(x) for x in line.split('x')) for line in puzzle.input_data.splitlines()]

sides = [
    [a * b for a, b in combinations(lengths, 2)]
    for lengths in data
]
puzzle.answer_a = sum(min(s) + 2 * sum(s) for s in sides)
puzzle.answer_b = sum(2 * (l + w) + l * w * h for l, w, h in data)
