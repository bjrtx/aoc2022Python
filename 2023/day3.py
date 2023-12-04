import itertools
import math

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)
data = puzzle.input_data.splitlines()


def is_symbol(i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[i]) and data[i][j] != '.' and not data[i][j].isnumeric()


total = 0
for i, row in enumerate(data):
    numbers = [list(g) for k, g in itertools.groupby(enumerate(row), lambda s: s[1].isnumeric()) if k]
    for g in numbers:
        begin, _ = g[0]
        end, _ = g[-1]
        if any(is_symbol(ii, jj) for ii in (i - 1, i, i + 1) for jj in range(begin - 1, end + 2)):
            total += int(row[begin:end + 1])

puzzle.answer_a = total

total = 0
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == '*':
            numbers = [(i, list(g)) for k, g in itertools.groupby(enumerate(row), lambda s: s[1].isnumeric()) if k]
            if i > 0:
                numbers += [(i - 1, list(g)) for k, g in
                            itertools.groupby(enumerate(data[i - 1]), lambda s: s[1].isnumeric()) if k]
            if i < len(data) - 1:
                numbers += [(i + 1, list(g)) for k, g in
                            itertools.groupby(enumerate(data[i + 1]), lambda s: s[1].isnumeric()) if k]

            numbers = [
                (ii, (g[0][0], g[-1][0])) for ii, g in numbers
                if g[0][0] - 1 <= j <= g[-1][0] + 1
            ]
            if len(numbers) == 2:
                total += math.prod(int(data[ii][begin:end + 1]) for ii, (begin, end) in numbers)

puzzle.answer_b = total
