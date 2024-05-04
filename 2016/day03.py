from itertools import chain

from more_itertools import chunked
from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=3)
data = puzzle.input_data.splitlines()

lines = [[int(x) for x in line.split()] for line in data]


def valid(line):
    a, b, c = sorted(line)
    return a + b > c


puzzle.answer_a = sum(valid(line) for line in lines)
puzzle.answer_b = sum(valid(t) for t in chunked(chain(*zip(*lines)), 3))
