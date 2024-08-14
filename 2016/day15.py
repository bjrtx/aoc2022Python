import re

from aocd.models import Puzzle
from sympy.ntheory.modular import crt

puzzle = Puzzle(year=2016, day=15)
data = puzzle.input_data.splitlines()

pattern = r'Disc #. has (\d+) positions; at time=0, it is at position (\d+).'
moduli, positions = zip(*
                        (map(int, re.fullmatch(pattern, line).groups())
                         for line in data)
                        )
remainders = tuple(-(x + i) for i, x in enumerate(positions, start=1))
puzzle.answer_a, _ = crt(moduli, remainders)
puzzle.answer_b, _ = crt(moduli + (11,), remainders + (-len(remainders) - 1,))


