import re
from collections import defaultdict
from math import prod

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=12)
data = puzzle.input_data.splitlines()


def run(c=0):
    regs = {k: 0 for k in 'abcd'}
    regs['c'] = c
    idx = 0
    while True:
        try:
            match data[idx].split():
                case ['cpy', x, y]:
                    regs[y] = regs[x] if x.isalpha() else int(x)
                case ['inc', x]:
                    regs[x] += 1
                case ['dec', x]:
                    regs[x] -= 1
                case ['jnz', x, y]:
                    if regs[x] if x.isalpha() else int(x):
                        idx += regs[y] if y.isalpha() else int(y)
                        continue
            idx += 1
        except IndexError:
            return regs['a']


puzzle.answer_a, puzzle.answer_b = run(), run(1)
