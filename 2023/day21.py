import nographs
import scipy
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=21)
data = puzzle.input_data.splitlines()
m = len(data)
start = (m // 2, m // 2)


def next_vertices(pos, strict):
    i, j = pos
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if not strict or i in range(m) and j in range(m):
            if data[x % m][y % m] != '#':
                yield x, y


def sphere(r, strict=False):
    traversal = nographs.TraversalBreadthFirst(lambda pos, _: next_vertices(pos, strict)).start_from(start)
    s = set(f for f in traversal.go_for_depth_range(0, r + 1) if not (traversal.depth + r) % 2)
    return s if r % 2 else s | {start}


puzzle.answer_a = len(sphere(64, strict=True))

# Took me about two days to get here...
a, b = zip(*((i, len(sphere(x))) for i, x in enumerate(range(65, 400, 131))))
puzzle.answer_b = int(scipy.interpolate.lagrange(a, b)((26501365 - 65) // 131))
