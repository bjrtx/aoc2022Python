import itertools

from sympy.ntheory.modular import crt
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=13)
data = puzzle.input_data.splitlines()

ranges = eval('{' + ','.join(data) + '}')

puzzle.answer_a = sum(
    r * d
    for r, d in ranges.items()
    if not (r % (2 * d - 2))
)

puzzle.answer_b = next(
    i
    for i in itertools.count()
    if all((i + r) % (2 * d - 2) for r, d in ranges.items())
)
