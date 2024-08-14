import itertools

from aocd.models import Puzzle
from more_itertools import quantify, ilen

puzzle = Puzzle(year=2019, day=4)
lo, hi = puzzle.input_data.split('-')


def non_decr(n, first=1):
    if n == 0:
        yield ''
    else:
        for d in range(first, 10):
            for s in non_decr(n - 1, first=d):
                yield str(d) + s


g = non_decr(6)
g = itertools.dropwhile(lambda x: x < lo, g)
g = itertools.takewhile(lambda x: x <= hi, g)
g, h = itertools.tee(
    [ilen(g) for _, g in itertools.groupby(x)]
    for x in g
)
puzzle.answer_a = quantify(any(z > 1 for z in x) for x in g)
puzzle.answer_b = quantify(2 in x for x in h)
