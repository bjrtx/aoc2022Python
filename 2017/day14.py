import itertools

import networkx as nx
import numpy as np
from aocd.models import Puzzle

from day10 import knot_hash

puzzle = Puzzle(year=2017, day=14)
data = puzzle.input_data

grid = np.array(
    [list(f"{int(knot_hash(f'{data}-{i}'), 16):0128b}") for i in range(128)]
) == '1'

puzzle.answer_a = int(np.sum(grid))

g = nx.Graph()
for i, row in enumerate(grid):
    for j, b in enumerate(row):
        if b:
            g.add_node((i, j))
            for neighb in [(i - 1, j), (i, j - 1)]:
                if neighb in g:
                    g.add_edge((i, j), neighb)

puzzle.answer_b = nx.components.number_connected_components(g)

