import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=12)
data = puzzle.input_data.splitlines()

g = nx.Graph()
for line in data:
    node, neighbours = line.split(' <-> ')
    g.add_edges_from((node, n) for n in neighbours.split(', '))

puzzle.answer_a = len(nx.components.node_connected_component(g, '0'))
puzzle.answer_b = nx.components.number_connected_components(g)
