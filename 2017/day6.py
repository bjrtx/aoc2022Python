import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=6)
data = [int(x) for x in puzzle.input_data.split()]

banks = data[:]
seen = {}
for step in itertools.count(1):
    print(banks)
    blocks = max(banks)
    index = banks.index(blocks)
    q, r = divmod(blocks, len(banks))
    for i in range(len(banks)):
        banks[i] += q
    for i in range(1, r + 1):
        banks[(index + i) % len(banks)] += 1
    banks[index] = q
    t = tuple(banks)
    if t in seen:
        break
    else:
        seen[t] = step

puzzle.answer_a = step
puzzle.answer_b = step - seen[t]