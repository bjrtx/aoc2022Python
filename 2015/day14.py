import re
from itertools import *

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=14)
data = puzzle.input_data

reindeer = [
    [int(i) for i in m.groups()]
    for m in re.finditer(r"can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", data)
]


def positions():
    speeds = [
        islice(
            cycle(chain(repeat(a, b), repeat(0, c))),
            2503
        )
        for a, b, c in reindeer
    ]
    return zip(*map(accumulate, speeds))



puzzle.answer_a = max(more_itertools.last(positions()))

scores = [0 for _ in reindeer]
for p in positions():
    m = max(p)
    for i, x in enumerate(p):
        scores[i] += x == m

puzzle.answer_b = max(scores)
