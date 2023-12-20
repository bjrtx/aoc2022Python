import itertools
import timeit

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=11)
data = puzzle.input_data.splitlines()

galaxies = [(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '#']
lines, columns = zip(*galaxies)
columns = sorted(columns)


def all_pairs_shortest_paths(weight):
    return sum(
        i * (len(galaxies) - i) * ((b - a - 1) * weight + 1)
        for axis in (lines, columns)
        for i, (a, b) in enumerate(itertools.pairwise(axis), start=1)
        if b > a
    )


puzzle.answer_a, puzzle.answer_b = map(all_pairs_shortest_paths, (2, 1_000_000))
