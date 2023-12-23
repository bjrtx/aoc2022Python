import heapq
from collections import defaultdict, deque

import more_itertools
from sortedcontainers import sorteddict
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=22)
bricks = [[eval(t) for t in line.split('~')] for line in puzzle.input_data.splitlines()]

h = [(min(a[-1], b[-1]), i, a, b) for i, (a, b) in enumerate(bricks)]
heapq.heapify(h)


def intersect(r1, r2):
    ((xa, ya), (xb, yb)), ((xc, yc), (xd, yd)) = r1, r2
    xmin = max(min(xa, xb), min(xc, xd))
    xmax = min(max(xa, xb), max(xc, xd))
    ymin = max(min(ya, yb), min(yc, yd))
    ymax = min(max(ya, yb), max(yc, yd))
    return xmin <= xmax and ymin <= ymax


by_highest_level = sorteddict.SortedDict(lambda height: -height)
support_of = defaultdict(set)
while h:
    _, i, (ax, ay, az), (bx, by, bz) = heapq.heappop(h)
    r = ((ax, ay), (bx, by))
    for top in by_highest_level:
        if below := {j for (j, rect) in by_highest_level[top] if intersect(r, rect)}:
            support_of[i] = below
            by_highest_level.setdefault(top + abs(az - bz) + 1, []).append((i, r))
            break
    else:
        by_highest_level.setdefault(abs(az - bz) + 1, []).append((i, r))

supported_by = defaultdict(set)
for x, v in support_of.items():
    for y in v:
        supported_by[y].add(x)

unremovable = set(more_itertools.flatten(v for v in support_of.values() if len(v) == 1))
puzzle.answer_a = len(bricks) - len(unremovable)


def cost(brick):
    fallen = {brick}
    q = deque(supported_by[brick])
    while q:
        next_ = q.popleft()
        if support_of[next_] <= fallen:
            fallen.add(next_)
            q.extend(supported_by[next_])
    return len(fallen) - 1


puzzle.answer_b = sum(cost(i) for i, _ in enumerate(bricks))
