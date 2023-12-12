import itertools
import re

import intervaltree
from aocd.models import Puzzle

puzzle = Puzzle(2022, 15)
data = puzzle.input_data
lines = data.splitlines()
sensor_and_ranges = {}
beacons = set()


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
for line in lines:
    x, y, xx, yy = map(int, re.fullmatch(pattern, line).groups())
    sensor_and_ranges[(x, y)] = abs(xx - x) + abs(yy - y)
    beacons.add((xx, yy))

print(sensor_and_ranges, beacons)
intervals = intervaltree.IntervalTree()
for (x, y), d in sensor_and_ranges.items():
    budget = d - abs(y - 2_000_000)
    if budget >= 0:
        intervals.addi(x - budget, x + budget)
intervals.merge_overlaps(strict=False)
puzzle.answer_a = sum(i.end - i.begin + 1 for i in intervals) - sum(y == 2_000_000 for _, y in beacons)


# question b
def all_candidates():
    for (x, y), r in sensor_and_ranges.items():
        for a, b in itertools.product((-1, 1), repeat=2):
            yield from ((x + a * t, y + b * (r + 1 - t)) for t in range(r + 2))


# not optimal, todo
unique_sol = set(
    (x, y)
    for x, y in all_candidates()
    if 0 <= x <= 4_000_000 and 0 <= y <= 4_000_000 and (x, y) not in beacons
    if all(distance((x, y), b) > r for b, r in sensor_and_ranges.items())
)
assert len(unique_sol) == 1
x, y = unique_sol.pop()
puzzle.answer_b = x * 4_000_000 + y
