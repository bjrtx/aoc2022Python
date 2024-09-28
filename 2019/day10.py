import itertools
import math
from collections import defaultdict

from aocd.models import Puzzle
from more_itertools import interleave_longest, nth

puzzle = Puzzle(year=2019, day=10)
data = puzzle.input_data.splitlines()

m, n = len(data), len(data[0])
asteroids = {
    (i, j)
    for i, row in enumerate(data)
    for j, x in enumerate(row)
    if x == '#'
}

mem = defaultdict(set)
for (x_a, y_a), (x_b, y_b) in itertools.permutations(asteroids, 2):
    x, y = (x_b - x_a, y_b - y_a)
    d = math.gcd(x, y)
    mem[(x_a, y_a)].add((x // d, y // d))
(x, y), v = max(mem.items(), key=lambda t: len(t[1]))
puzzle.answer_a = len(v)

asteroids.remove((x, y))
by_dir = defaultdict(list)
for xx, yy in asteroids:
    a, b = (xx - x, yy - y)
    d = math.gcd(a, b)
    by_dir[a // d, b // d].append((xx, yy))

stacks = [
    sorted(by_dir[k], key=lambda t: abs(t[0] - x) + abs(t[1] - y))
    for k in sorted(by_dir.keys(), key=lambda t: -math.atan2(t[1], t[0]))
]
y, x = nth(interleave_longest(*stacks), 199)
puzzle.answer_b = x * 100 + y
