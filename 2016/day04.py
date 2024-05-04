import re
from collections import Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=4)
data = puzzle.input_data.splitlines()


def parse(room):
    letters, rem = room.rsplit('-', 1)
    id_, checksum = re.match(r'(\d+)\[(.*)]', rem).groups()
    return int(id_), letters, checksum


def validate(letters, checksum):
    in_order = sorted((-v, k) for k, v in Counter(letters).items() if k != '-')
    most_common = ''.join(k for v, k in in_order[:5])
    return checksum == most_common


def decrypt(letters, id_):
    def chars():
        for c in letters:
            if c == '-':
                yield ' '
            else:
                yield chr(ord('a') + (ord(c) - ord('a') + id_) % 26)

    return ''.join(chars())


puzzle.answer_a = sum(id_ for id_, letters, checksum in map(parse, data) if validate(letters, checksum))
puzzle.answer_b = next(
    id_
    for id_, letters, checksum in map(parse, data)
    if 'north' in decrypt(letters, id_)
)
