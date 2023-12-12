import itertools
import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=7)
data = puzzle.input_data.splitlines()

nodes = {}
for line in data:
    name, _, out = line.partition('->')
    out = out.strip().split(', ') if out else ''
    print(name, out)
    name, weight = re.match(r'(\w+) \((\d+)\)', name).groups()
    nodes[name] = (weight, out)

have_incoming = set(itertools.chain.from_iterable(out for _, out in nodes.values()))
puzzle.answer_a = more_itertools.one(set(nodes.keys()) - have_incoming)
