from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=2)
res = 0

for line in puzzle.input_data.splitlines():
    l, w, h = map(int, line.split('x'))
    sides = (l * w, l * h, w * h)
    res += min(sides) + 2 * sum(sides)
puzzle.answer_a = res

res = 0
for line in puzzle.input_data.splitlines():
    l, w, h = sorted(map(int, line.split('x')))
    res += 2 * (l + w) + l * w * h
puzzle.answer_b = res
