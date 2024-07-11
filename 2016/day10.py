import re
from collections import defaultdict
from math import prod

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=10)
data = puzzle.input_data.splitlines()

values, dest = defaultdict(list), {}
pattern = r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'
for line in data:
    m = re.fullmatch(r'value (\d+) goes to bot (\d+)', line)
    if m:
        values[m[2]].append(int(m[1]))
    else:
        assert (m := re.fullmatch(pattern, line))
        dest[m[1]] = ['o' * (m[2] == 'output') + m[3], 'o' * (m[4] == 'output') + m[5]]

while (curr := next((k for k, v in values.items() if len(v) == 2), None)) is not None:
    values[curr].sort()
    if values[curr] == [17, 61]:
        puzzle.answer_a = int(curr)
    for x, d in zip(values[curr], dest[curr]):
        values[d].append(x)
    values[curr].clear()

puzzle.answer_b = prod(values[f'o{i}'][0] for i in range(3))
