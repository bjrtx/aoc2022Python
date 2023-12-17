from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=17)
data = tuple(int(x) for x in puzzle.input_data.splitlines())


@cache
def solutions(amount, sizes=tuple(data)):
    if amount == 0:
        return (0,)
    elif amount < 0 or not sizes:
        return ()
    else:
        return (
                tuple(a + 1 for a in solutions(amount - sizes[0], sizes[1:]))
                + solutions(amount, sizes[1:])
        )


t = solutions(150)
puzzle.answer_a = len(t)
puzzle.answer_b = t.count(min(t))
