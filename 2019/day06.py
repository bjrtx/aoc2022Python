from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)
data = puzzle.input_data.splitlines()

center = dict(line.split(')')[::-1] for line in data)


@cache
def orbits(body):
    p = center.get(body, None)
    return 0 if p is None else orbits(p) + 1


puzzle.answer_a = sum(orbits(b) for b in center)


def parents(body):
    while (body := center.get(body, None)) is not None:
        yield body


puzzle.answer_b = len(set(parents('SAN')) ^ set(parents('YOU')))
