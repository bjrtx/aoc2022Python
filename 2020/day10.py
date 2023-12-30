import itertools
from collections import Counter
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=10)
data = [int(x) for x in puzzle.input_data.splitlines()]
max_ = max(data) + 3
values = set(itertools.chain(data, (0, max_)))

c = Counter(b - a for a, b in itertools.pairwise(sorted(values)))
puzzle.answer_a = c[1] * c[3]


@cache
def paths(source):
    if source == max_:
        return 1
    else:
        return sum(
            paths(n)
            for n in range(source + 1, source + 4)
            if n in values
        )


puzzle.answer_b = paths(0)
