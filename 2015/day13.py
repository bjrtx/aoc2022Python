import functools
import itertools
import json
import operator
import re
from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=13)
data = puzzle.input_data

changes = defaultdict(int)

for m in re.finditer(r"(\w+) would (gain|lose) (\d+) happiness unit.? by sitting next to (\w+).", data):
    changes[frozenset((m[1], m[4]))] += (1 if m[2] == "gain" else -1) * int(m[3])


def value(permutation):
    permutation = list(permutation)
    return (sum(changes[frozenset((a, b))] for a, b in itertools.pairwise(permutation))
            +
            changes[frozenset((permutation[0], permutation[-1]))]
            )


names = functools.reduce(operator.or_, changes.keys())
puzzle.answer_a = max(value(p) for p in itertools.permutations(names))
puzzle.answer_b = max(value(p) for p in itertools.permutations(names | {'me'}))
