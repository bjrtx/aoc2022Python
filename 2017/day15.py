import itertools
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=15)
data = puzzle.input_data

inputs = [int(x) for x in re.findall(r'\d+', data)]


def gen_a(filter=False):
    a, _ = inputs
    while True:
        a = a * 16807 % 2147483647
        if not (filter and a % 4):
            yield a


def gen_b(filter=False):
    _, b = inputs
    while True:
        b = b * 48271 % 2147483647
        if not (filter and b % 8):
            yield b


puzzle.answer_a = sum(
    a & ((1 << 16) - 1) == b & ((1 << 16) - 1)
    for a, b in itertools.islice(zip(gen_a(), gen_b()), 40_000_000)
)
puzzle.answer_b = sum(
    a & ((1 << 16) - 1) == b & ((1 << 16) - 1)
    for a, b in itertools.islice(zip(gen_a(filter=True), gen_b(filter=True)), 5_000_000)
)