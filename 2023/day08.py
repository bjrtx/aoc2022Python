import itertools
import math
import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=8)
data = puzzle.input_data

edges = {m[1]: (m[2], m[3]) for m in re.finditer(r'(\w+) = \((\w+), (\w+)\)', data)}
instructions = "".join(line for line in data.splitlines() if '=' not in line)

curr = 'AAA'
for i, step in enumerate(itertools.cycle(instructions)):
    if curr == 'ZZZ':
        break
    curr = edges[curr][step == 'R']

# noinspection PyUnboundLocalVariable
puzzle.answer_a = i


def distances_to_z(k):
    curr = k
    seen = set()
    for i, step in enumerate(itertools.cycle(instructions)):
        aug_step = (curr, i % len(instructions))
        if aug_step in seen:
            break
        elif curr.endswith('Z'):
            yield i
        curr = edges[curr][step == 'R']
        seen.add(aug_step)


distances = [list(distances_to_z(k)) for k in edges.keys() if k.endswith('A')]  # all singletons
puzzle.answer_b = math.lcm(*more_itertools.flatten(distances))
