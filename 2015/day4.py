import itertools
from hashlib import md5

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=4)
data = puzzle.input_data.strip()

puzzle.answer_a = next(
    i
    for i in itertools.count(1)
    if md5(f"{data}{i}".encode()).hexdigest().startswith("00000")
)
puzzle.answer_b = next(
    i
    for i in itertools.count(1)
    if md5(f"{data}{i}".encode()).hexdigest().startswith("000000")
)
