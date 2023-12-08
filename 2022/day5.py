import re
from copy import deepcopy

from aocd.models import Puzzle

puzzle = Puzzle(2022, 5)
data = puzzle.input_data.splitlines()
stack_depth, index_line = next((i, line) for i, line in enumerate(data) if line.startswith(" 1   2"))
num_stacks = int(index_line.split()[-1])


def build_stack(index):
    chars = [line[index * 4 - 3] for line in data[:stack_depth]]
    return [c for c in chars if c.isalpha()]


stacks = [list(reversed(build_stack(i))) for i in range(1, num_stacks + 1)]

pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
instructions = [[int(x) for x in pattern.fullmatch(line).groups()] for line in data[stack_depth + 2:]]

stacks_a = deepcopy(stacks)
stacks_b = deepcopy(stacks)
for a, b, c in instructions:
    tmp = []
    for _ in range(a):
        stacks_a[c - 1].append(stacks_a[b - 1].pop())
        tmp.append(stacks_b[b - 1].pop())
    stacks_b[c - 1] += reversed(tmp)

puzzle.answer_a = "".join(s[-1] for s in stacks_a)
puzzle.answer_b = "".join(s[-1] for s in stacks_b)
