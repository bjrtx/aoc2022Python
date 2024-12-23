import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=23)
data = puzzle.input_data.splitlines()

g = nx.Graph(line.split('-', 1) for line in data)
puzzle.answer_a = sum(
    6 // (1 + sum(v.startswith('t') for v in e))
    for n in g
    if n.startswith('t')
    for e in nx.induced_subgraph(g, g[n]).edges
) // 6

c, _ = nx.max_weight_clique(g, weight=None)
puzzle.answer_b = ','.join(sorted(c))
