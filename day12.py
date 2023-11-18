import itertools
from collections import deque
import networkx as nx


from aocd.models import Puzzle

puzzle = Puzzle(2022, 12)
data = puzzle.input_data

matrix = [list(s) for s in data.splitlines()]
m = len(matrix)
n = len(matrix[0])

start = next((i, j) for i, row in enumerate(matrix) for j, x in enumerate(row) if x == 'S')
goal = next((i, j) for i, row in enumerate(matrix) for j, x in enumerate(row) if x == 'E')

G = nx.DiGraph()
G.add_nodes_from(
    ((i, j), {"value": ord('a' if x == 'S' else 'z' if x == 'E' else x)})
    for i, row in enumerate(matrix)
    for j, x in enumerate(row)
)
for (i, j) in G.nodes:
    elevation = G.nodes[(i, j)]["value"]
    neighbours = [
        (ii, jj)
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if (ii, jj) in G.nodes and G.nodes[(ii, jj)]["value"] < elevation + 2
    ]
    G.add_edges_from(((i, j), n) for n in neighbours)

puzzle.answer_a = nx.algorithms.shortest_path_length(G, source=start, target=goal)
lowest_points = [n for n, v in G.nodes.items() if v["value"] == ord('a')]
puzzle.answer_b = min(l for source, l in nx.algorithms.shortest_path_length(G, target=goal).items() if source in lowest_points)
