from functools import cache

import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=12)
data = puzzle.input_data.splitlines()

g = nx.Graph(line.split('-', 1) for line in data)


@cache
def paths(n='start', can_double=False, doublet=None, past=frozenset()):
    if n == 'end':
        return doublet is None or doublet in past
    else:
        res = 0
        if n.islower():
            if can_double and doublet is None and n not in ('start', 'end'):
                res = sum(paths(nb, True, doublet=n, past=past) for nb in g[n].keys() - past)
            past |= {n}
        res += sum(paths(nb, can_double, doublet=doublet, past=past) for nb in g[n].keys() - past)
        return res


puzzle.answer_a, puzzle.answer_b = (paths(can_double=b) for b in (False, True))
