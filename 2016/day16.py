import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=16)
data = puzzle.input_data


def dragon_curve(init, length):
    str = init
    while len(str) < length:
        str += '0' + ''.join(reversed(str.translate({ord('0'): '1', ord('1'): '0'})))
    return str[:length]


def checksum(str):
    while len(str) % 2 == 0:
        str = ''.join('1' if a == b else '0' for a, b in itertools.batched(str, 2))
    return str


puzzle.answer_a = checksum(dragon_curve(data, 272))
puzzle.answer_b = checksum(dragon_curve(data, 35651584))
