import itertools
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)
data = puzzle.input_data

lines = [
    tuple(map(int, m.groups()))
    for m in re.finditer(r"(\d+),(\d+) -> (\d+),(\d+)", data)
]
lines = [
    sorted(((xa, ya), (xb, yb))) for xa, ya, xb, yb in lines
]


def is_horizontal(line): return line[0][0] == line[1][0]


def is_vertical(line): return line[0][1] == line[1][1]


def is_axis_parallel(line): return is_horizontal(line) or is_vertical(line)


def intersect(la, lb):
    (xa1, ya1), (xa2, ya2) = la
    (xb1, yb1), (xb2, yb2) = lb
    if is_horizontal(la):
        if xb1 <= xa1 <= xb2:
            if is_horizontal(lb):
                for y in range(max(ya1, yb1), min(ya2, yb2) + 1):
                    yield xa1, y
            elif is_vertical(lb):
                if ya1 <= yb1 <= ya2:
                    yield xa1, yb1
            else:
                y = (1 if yb2 >= yb1 else -1) * (xa1 - xb1) + yb1
                if ya1 <= y <= ya2 or ya2 <= y <= ya1:
                    yield xa1, y
    elif is_vertical(la):
        for x, y in intersect(sorted([(ya1, xa1), (ya2, xa2)]), sorted([(yb1, xb1), (yb2, xb2)])):
            yield y, x
    elif is_axis_parallel(lb):
        yield from intersect(lb, la)
    else:
        lla = sorted([(xa1 + ya1, xa1 - ya1), (xa2 + ya2, xa2 - ya2)])
        llb = sorted([(xb1 + yb1, xb1 - yb1), (xb2 + yb2, xb2 - yb2)])
        assert is_axis_parallel(lla) and is_axis_parallel(llb)
        for x, y in intersect(lla, llb):
            qx, rx = divmod(x + y, 2)
            qy, ry = divmod(x - y, 2)
            if not rx and not ry:
                yield qx, qy


points = {
    x for la, lb in itertools.combinations(filter(is_axis_parallel, lines), 2) for x in intersect(la, lb)
}

puzzle.answer_a = len(set(
    itertools.chain.from_iterable(
        intersect(la, lb) for la, lb in itertools.combinations(filter(is_axis_parallel, lines), 2))
))

puzzle.answer_b = len(set(
    itertools.chain.from_iterable(intersect(la, lb) for la, lb in itertools.combinations(lines, 2))
))
