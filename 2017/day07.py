import collections
import itertools
import re
from functools import cache

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=7)
data = puzzle.input_data.splitlines()

nodes = {}
parent = {}
for line in data:
    name, _, out = line.partition('->')
    out = out.strip().split(', ') if out else ''
    name, weight = re.match(r'(\w+) \((\d+)\)', name).groups()
    nodes[name] = (int(weight), out)
    parent.update((n, name) for n in out)


have_incoming = set(itertools.chain.from_iterable(out for _, out in nodes.values()))
puzzle.answer_a = more_itertools.one(set(nodes) - have_incoming)


@cache
def tower_weight(node):
    weight, out = nodes[node]
    return weight + sum(tower_weight(n) for n in out)


for node, (_, out) in nodes.items():
    c = collections.Counter(tower_weight(n) for n in out)
    if len(out) > 1 and 1 in c.values():
        tw = next(k for k, v in c.items() if v == 1)
        defect = next(n for n in out if tower_weight(n) == tw)
        other_tw = next(k for k, v in c.items() if v != 1)
        w, _ = nodes[defect]
        puzzle.answer_b = other_tw - tw + w
        break
