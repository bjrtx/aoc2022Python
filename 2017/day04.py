from more_itertools import all_unique
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=4)
data = puzzle.input_data.splitlines()


puzzle.answer_a = sum(all_unique(passphrase.split()) for passphrase in data)
puzzle.answer_b = sum(all_unique(tuple(sorted(w)) for w in passphrase.split()) for passphrase in data)
