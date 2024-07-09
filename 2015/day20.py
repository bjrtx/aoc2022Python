from aocd.models import Puzzle
from sympy.functions.combinatorial.numbers import divisor_sigma

puzzle = Puzzle(year=2015, day=20)
data = int(puzzle.input_data)

puzzle.answer_a = next(
    i
    for i in range(1, data)
    if divisor_sigma(i) * 10 >= data
)


def house_score(h):
    return 11 * sum(
        q
        for q, r in (divmod(h, i) for i in range(1, 51))
        if not r
    )


puzzle.answer_b = next(i for i in range(1, data) if house_score(i) >= data)
