import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=3)
data = puzzle.input_data

s = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)

puzzle.answer_a = sum(int(m[0]) * int(m[1]) for m in s)

res = 0
count = True
for m in re.finditer(r'(mul)\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', data):
    if m[1] == 'mul':
        if count:
            res += int(m[2]) * int(m[3])
    else:
        count = m[0] == 'do()'

puzzle.answer_b = res
