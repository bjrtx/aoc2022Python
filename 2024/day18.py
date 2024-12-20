import itertools

import networkx as nx
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=18)
data = puzzle.input_data

bytes_ = [eval(row) for row in data.splitlines()]

n = 71
memory_space = np.ones((n, n), dtype=np.bool_)
x, y = zip(*bytes_[:1024])
memory_space[x, y] = np.False_


def next_vertices(pos):
    i, j = pos
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if x in range(n) and y in range(n) and memory_space[x, y]:
            yield x, y


g = nx.Graph(
    (pos, n)
    for pos in itertools.product(range(n), repeat=2)
    if memory_space[pos]
    for n in next_vertices(pos))

puzzle.answer_a = nx.shortest_path_length(g, (0, 0), (n - 1, n - 1))

# Inefficient, but not too inefficient
for b in bytes_[1024:]:
    g.remove_node(b)
    if not nx.has_path(g, (0, 0), (n - 1, n - 1)):
        puzzle.answer_b = f'{b[0]},{b[1]}'
        break
