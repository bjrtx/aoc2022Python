import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=14)

data = list(more_itertools.split_before(
    puzzle.input_data.splitlines(),
    lambda s: s.startswith('mask')
))

mem = {}
for mask, *instructions in data:
    mask = mask.strip('mask = ')
    zero_pos = [i for i, c in enumerate(reversed(mask)) if c == '0']
    one_pos = [i for i, c in enumerate(reversed(mask)) if c == '1']
    zero_mask = 2 ** 36 + ~sum(2 ** i for i in zero_pos)
    one_mask = sum(2 ** i for i in one_pos)
    for line in instructions:
        address, value = map(int, re.fullmatch(r'mem\[(\d+)] = (\d+)', line).groups())
        mem[address] = (value | one_mask) & zero_mask
puzzle.answer_a = sum(mem.values())


def all_values(mask, value):
    value |= sum(2 ** i for i, c in enumerate(reversed(mask)) if c == '1')
    vals = [value]
    for i, c in enumerate(reversed(mask)):
        if c == 'X':
            vals += [v ^ 2 ** i for v in vals]
    return vals


mem = {}
for mask, *instructions in data:
    for line in instructions:
        address, value = map(int, re.fullmatch(r'mem\[(\d+)] = (\d+)', line).groups())
        for v in all_values(mask.strip('mask = '), address):
            mem[v] = value
puzzle.answer_b = sum(mem.values())
