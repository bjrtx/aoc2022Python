import itertools
import math

import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=25)

g = nx.Graph(
    itertools.chain.from_iterable(
        itertools.product((a,), b.split(' '))
        for a, b in (line.split(': ') for line in puzzle.input_data.splitlines())
    )
)
g.remove_edges_from(nx.minimum_edge_cut(g))
puzzle.answer_a = math.prod(len(c) for c in nx.connected_components(g))
