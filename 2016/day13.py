import itertools

from aocd.models import Puzzle
from more_itertools import first, nth

puzzle = Puzzle(year=2016, day=13)
data = int(puzzle.input_data)


def neighbours(x, y):
    for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if i >= 0 and j >= 0 and not (
                ((i + j) ** 2 + 3 * i + j + data).bit_count() % 2):
            yield i, j


def frontiers():
    seen = set()
    frontier = {(1, 1)}
    for _ in itertools.count():
        yield frontier, seen
        seen |= frontier
        frontier = {n for p in frontier for n in neighbours(*p) if n not in seen}


puzzle.answer_a = first(i for i, (f, _) in enumerate(frontiers()) if (31, 39) in f)
puzzle.answer_b = len(nth(frontiers(), 51)[1])
