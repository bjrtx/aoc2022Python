import itertools
from collections import Counter
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=14)
data = puzzle.input_data

template, rules = data.split('\n\n')
rules = (line.split(' -> ', 1) for line in rules.splitlines())
rules = {tuple(a): b for a, b in rules}


@cache
def step(a, b, n):
    if n == 0 or (a, b) not in rules:
        return Counter((a, b))
    else:
        c = rules[a, b]
        d = step(a, c, n - 1) + step(c, b, n - 1)
        d[c] -= 1
        return d


def evolve(n):
    res = Counter((template[0]))
    for a, b in itertools.pairwise(template):
        res += (step(a, b, n))
        res[a] -= 1
    v = res.values()
    return max(v) - min(v)


puzzle.answer_a, puzzle.answer_b = evolve(10), evolve(40)
