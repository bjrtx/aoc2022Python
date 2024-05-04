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
                    row = max(0, row - v)
                case 'D':
                    row = min(2, row + v)
                case 'L':
                    col = max(0, col - v)
                case 'R':
                    col = min(2, col + v)
        yield row * 3 + col + 1


puzzle.answer_a = ''.join(map(str, positions()))


def positions2():
    layout = [
        'xx1xx', 'x234x', '56789', 'xABCx', 'xxDxx'
    ]
    row, col = 0, -2
    for w in data:
        for c, g in itertools.groupby(w):
            v = more_itertools.ilen(g)
            match c:
                case 'U':
                    row = max(row - v, abs(col) - 2)
                case 'D':
                    row = min(row + v, 2 - abs(col))
                case 'L':
                    col = max(col - v, abs(row) - 2)
                case 'R':
                    col = min(col + v, 2 - abs(row))

        yield layout[row + 2][col + 2]


puzzle.answer_b = ''.join(map(str, positions2()))
