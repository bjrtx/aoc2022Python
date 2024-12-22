import itertools
from collections import Counter

from more_itertools import iterate, nth, windowed
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=22)
data = [int(x) for x in puzzle.input_data.splitlines()]


def evolve(secret):
    mask = (1 << 24) - 1
    secret ^= (secret << 6) & mask
    secret ^= secret >> 5
    secret ^= (secret << 11) & mask
    return secret


puzzle.answer_a = sum(nth(iterate(evolve, secret), 2000) for secret in data)

c = Counter()
for secret in data:
    seen = set()
    sequence = itertools.islice(iterate(evolve, secret), 2000)
    prices = [x % 10 for x in sequence]
    changes = (b - a for a, b in itertools.pairwise(prices))
    for s, p in zip(windowed(changes, 4), prices[4:]):
        if s not in seen:
            seen.add(s)
            c[s] += p

puzzle.answer_b = max(c.values())
