from collections import Counter
from statistics import mode

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=6)
data = puzzle.input_data.splitlines()


def least_common(t):
    return min((v, k) for k, v in Counter(t).items())[1]


puzzle.answer_a = ''.join(mode(col) for col in zip(*data))
puzzle.answer_b = ''.join(least_common(col) for col in zip(*data))
