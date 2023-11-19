import itertools
import re
import intervaltree
import tqdm as tqdm

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

intervals.clear()
def coords_to_one_d(a, b):
    return 4_000_000 * a + b  # ever so slightly off, not in any way that matters

intervals.addi(0, coords_to_one_d(4_000_000, 4_000_000))
for (x, y), d in tqdm.tqdm(sensor_and_ranges.items()):
    for l in range(-d, d + 1):
        if 0 <= x + l <= 4_000_000 and 0 <= x + l <= 4_000_000:
            intervals.chop(coords_to_one_d(x + l, max(0, y - (d - l))), coords_to_one_d(x + l, min(4000_000, y + (d - l))) + 1)
for (i, j) in beacons:
    intervals.chop(coords_to_one_d(i, j), coords_to_one_d(i, j) + 1)
intervals.merge_overlaps()
for i in intervals:
    print(i)
