import collections
import itertools
import re
from functools import cache

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=8)
data = puzzle.input_data.splitlines()


regs = collections.defaultdict(int)
m = 0
for line in data:
    reg, op, val, _, reg_cond, op_cond, val_cond = line.split()
    if eval(f'{regs[reg_cond]} {op_cond} {val_cond}'):
        regs[reg] += int(val) if op == 'inc' else -int(val)
        m = max(m, regs[reg])

puzzle.answer_a, puzzle.answer_b = max(regs.values()), m