import itertools
from hashlib import md5

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=4)
data = puzzle.input_data.strip()


def solve(zeroes):
    return next(
        i
        for i in itertools.count(1)
        if md5(f"{data}{i}".encode()).hexdigest().startswith("0" * zeroes)
    )


puzzle.answer_a, puzzle.answer_b = solve(5), solve(6)
