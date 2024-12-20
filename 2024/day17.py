import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=17)
data = re.match(r"""Register A: (\d+)
Register B: 0
Register C: 0

Program: ((\d,)*\d)""", puzzle.input_data)
reg_a = int(data[1])
prog = eval(data[2])


def run(a=reg_a):
    regs = {'a': a, 'b': 0, 'c': 0}
    idx = 0

    def get_combo(index):
        x = prog[index]
        if x <= 3:
            return x
        elif x <= 6:
            return regs['abc'[x - 4]]

    while True:
        try:
            match prog[idx]:
                case 0:
                    regs['a'] >>= get_combo(idx + 1)
                case 1:
                    regs['b'] ^= prog[idx + 1]
                case 2:
                    regs['b'] = get_combo(idx + 1) & 7
                case 3:
                    if regs['a']:
                        idx = prog[idx + 1] - 2
                case 4:
                    _ = prog[idx + 1]
                    regs['b'] ^= regs['c']
                case 5:
                    yield get_combo(idx + 1) & 7
                case 6:
                    regs['b'] = regs['a'] >> get_combo(idx + 1)
                case 7:
                    regs['c'] = regs['a'] >> get_combo(idx + 1)
            idx += 2
        except IndexError:
            return regs['a']


puzzle.answer_a = ','.join(map(str, run()))

# One observes that the program is a loop on the value of reg. A,
# where this value is divided by 8 at each iteration and the output
# of each iteration depends only on the first 10 bits of A.
# With my input, the program was equivalent to:
#   while a:
#       q, r = divmod(a, 8)
#       yield (r ^ (a >> (r ^ 7))) & 7
#       a = q

allowed = set(range(128))
for i in range(1, len(prog) + 1):
    allowed = [
        d * 8 + k
        for k in range(8)
        for d in allowed
        if more_itertools.iequals(run(d * 8 + k), prog[-i:])]
puzzle.answer_b = min(allowed)
