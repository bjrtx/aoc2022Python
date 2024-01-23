from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=2)
data = [sorted(int(x) for x in line.split('x')) for line in puzzle.input_data.splitlines()]

res = 0
for l, w, h in data:
    sides = (l * w, l * h, w * h)
    res += min(sides) + 2 * sum(sides)
puzzle.answer_a = res

res = 0
for l, w, h in data:
    res += 2 * (l + w) + l * w * h
puzzle.answer_b = res
