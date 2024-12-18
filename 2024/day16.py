import numpy as np
import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=16)
data = puzzle.input_data

map_ = np.array([list(row) for row in data.splitlines()])
m, n = map_.shape

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = *np.argwhere(map_ == 'S')[0], 0
end = np.argwhere(map_ == 'E')[0]

maze = nx.Graph()
for i, j in np.argwhere(map_ != '#'):
    for d, (dx, dy) in enumerate(dirs):
        ii, jj = i + dx, j + dy
        if 0 <= ii < m and 0 <= jj < n and map_[ii, jj] != '#':
            maze.add_edge((i, j, d), (ii, jj, d), weight=1)
        for eps in (1, -1):
            maze.add_edge((i, j, d), (i, j, (d + eps) % 4), weight=1_000)

for d in range(4):
    maze.add_edge((*end, d), 'end', weight=0)

puzzle.answer_a = m = nx.shortest_path_length(maze, source=start, target='end', weight='weight')
dist_to_end = dict(nx.single_source_dijkstra_path_length(maze, source='end', weight='weight'))
dist_to_start = dict(nx.single_source_dijkstra_path_length(maze, source=start, weight='weight'))
res = {
    n[:2]
    for n in dist_to_end
    if dist_to_end[n] + dist_to_start[n] == m
}
puzzle.answer_b = len(res) - 1
