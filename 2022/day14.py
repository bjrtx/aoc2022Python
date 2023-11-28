import itertools
from functools import cmp_to_key

from aocd.models import Puzzle

puzzle = Puzzle(2022, 14)
data = puzzle.examples[0].input_data

paths = [[eval(pair) for pair in l.split('->')] for l in data.splitlines()]
print(paths)

class Walls():
    def __init__(self):
        lines = [list(itertools.pairwise(l)) for l in paths]
        print(lines)
        self.pairs = list(itertools.chain.from_iterable(lines))
        print(self.pairs)

    def __contains__(self, item):
        x, y = item
        return any(
            a == c == x and ((b <= y <= d) or (d <= y <= b))
            or b == d == y and ((a <= x <= c) or (c <= x <= a))
            for (a, b), (c, d) in self.pairs
        )


walls = Walls()
bottom = max(y for _, y in itertools.chain(*walls.pairs)) + 1
print("bottom", bottom)

visited = set()


def flow(i, j):
    if (i, j) in walls or visited:
        print("collide", i, j)
        return
    yield from flow(i, j + 1)
    yield from flow(i - 1, j + 1)
    yield from flow(i + 1, j + 1)
    visited.add((i, j))
    yield i, j


_ = list(itertools.takewhile(lambda p:p[1] < bottom, flow(500, 0)))
print(len(visited))

