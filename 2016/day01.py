from aocd.models import Puzzle
from more_itertools import first, last, duplicates_everseen

puzzle = Puzzle(year=2016, day=1)
data = puzzle.input_data.split(', ')


def positions():
    dx, dy = (0, 1)
    x, y = 0, 0
    for w in data:
        dx, dy = (-dy, dx) if w[0] == 'L' else (dy, -dx)
        for _ in range(int(w[1:])):
            x += dx
            y += dy
            yield x, y


puzzle.answer_a = sum(map(abs, last(positions())))
puzzle.answer_b = sum(map(abs, first(duplicates_everseen(positions()))))
