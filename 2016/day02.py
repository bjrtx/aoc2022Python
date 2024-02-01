import itertools

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=2)
data = puzzle.input_data.splitlines()


def positions():
    row, col = 1, 1
    for w in data:
        for c, g in itertools.groupby(w):
            v = more_itertools.ilen(g)
            match c:
                case 'U':
                    row -= v
                case 'D':
                    row += v
                case 'L':
                    col -= v
                case 'R':
                    col += v
            row = min(max(0, row), 2)
            col = min(max(0, col), 2)
        yield row * 3 + col + 1


puzzle.answer_a = ''.join(map(str, positions()))
