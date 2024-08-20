import itertools

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)
data = [int(line) for line in puzzle.input_data.splitlines()]

puzzle.answer_a = sum(x // 3 - 2 for x in data)
puzzle.answer_b = sum(
    sum(
        itertools.takewhile(
            lambda x: x > 0,
            itertools.islice(more_itertools.iterate(lambda x: x // 3 - 2, first), 1, None)
        )
    )
    for first in data
)