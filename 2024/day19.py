from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=19)
data = puzzle.input_data

patterns, designs = data.split('\n\n')
patterns = set(patterns.split(', '))
designs = designs.splitlines()


@cache
def num_ways(design):
    return 1 if not design else sum(
        num_ways(design.removeprefix(p))
        for p in patterns
        if design.startswith(p)
    )


puzzle.answer_a = sum(bool(num_ways(d)) for d in designs)
puzzle.answer_b = sum(num_ways(d) for d in designs)
