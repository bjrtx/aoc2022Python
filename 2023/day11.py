import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=11)
data = puzzle.input_data.splitlines()

galaxies = [(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '#']


def all_pairs_shortest_paths(weight):
    lines, columns = zip(*galaxies)
    n_galaxies = len(galaxies)
    columns = sorted(columns)
    return sum(
        i * (n_galaxies - i) * ((b - a - 1) * weight + 1)
        for axis in (lines, columns)
        for i, (a, b) in enumerate(itertools.pairwise(axis), start=1)
        if b > a
    )


puzzle.answer_a = all_pairs_shortest_paths(2)
puzzle.answer_b = all_pairs_shortest_paths(1_000_000)
