import itertools
import math
import operator
import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=16)
data = puzzle.input_data.splitlines()
rules, ticket, others = more_itertools.split_at(data, pred=operator.not_)

ranges = dict()
for r in rules:
    field, a, b, c, d = re.fullmatch(r'([ a-z]*): (\d+)-(\d+) or (\d+)-(\d+)', r).groups()
    ranges[field] = (range(int(a), int(b) + 1), range(int(c), int(d) + 1))

ticket = eval(ticket[1])

invalid = sum(x for l in others[1:] for x in eval(l) if not any(x in r for r in itertools.chain(*ranges.values())))
puzzle.answer_a = invalid

possible = [list(ranges) for _ in ranges]
for t in others[1:]:
    t = eval(t)
    if any(not any(x in r for r in itertools.chain(*ranges.values())) for x in t):
        continue
    for i, x in enumerate(t):
        possible[i] = [f for f in possible[i] if any(x in r for r in ranges[f])]
l = list(enumerate(possible))
fixed = {}
while len(fixed) < len(ranges):
    l = [(i, [x for x in v if x not in fixed]) for i, v in l]
    fixed.update((v[0], i) for i, v in l if len(v) == 1)
puzzle.answer_b = math.prod(ticket[i] for v, i in fixed.items() if v.startswith('departure'))
