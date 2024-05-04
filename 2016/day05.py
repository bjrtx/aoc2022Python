from hashlib import md5
from itertools import count

from aocd.models import Puzzle
from more_itertools import take

puzzle = Puzzle(year=2016, day=5)
data = puzzle.input_data


def hashes():
    for idx in count():
        h = md5(f'{data}{idx}'.encode()).hexdigest()
        if h.startswith('00000'):
            yield h


puzzle.answer_a = ''.join(h[5] for h in take(8, hashes()))

chars = [None for _ in range(8)]
for h in hashes():
    i, v = h[5:7]
    if i in '01234567' and chars[int(i)] is None:
        chars[int(i)] = v
        if all(chars):
            break
puzzle.answer_b = ''.join(chars)