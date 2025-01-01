import itertools

from more_itertools import ilen, iterate, nth
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=10)
data = puzzle.input_data.strip()


def look_and_say(it):
    for k, g in itertools.groupby(it):
        yield sum(1 for _ in g)
        yield int(k)


s = nth(iterate(look_and_say, data), 40)
puzzle.answer_a = ilen(s)

s = nth(iterate(look_and_say, data), 50)
puzzle.answer_b = ilen(s)
