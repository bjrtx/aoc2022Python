from collections import Counter

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(2022, 6)
data = puzzle.input_data


def first_full(n):
    def lengths():
        starting = Counter(data[:n])
        yield len(+starting)
        for a, b in zip(data, data[n:]):
            starting[a] -= 1
            starting[b] += 1
            yield len(+starting)

    return n + next(more_itertools.iter_index(lengths(), n))


puzzle.answer_a = first_full(4)
puzzle.answer_b = first_full(14)
