import re

from aocd.models import Puzzle
from z3 import Ints, Optimize

puzzle = Puzzle(year=2024, day=13)
data = puzzle.input_data

machines = re.findall(
    r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""", data)


def solve(offset):
    res = 0
    a, b, c = Ints('a b c')
    for m in machines:
        dxa, dya, dxb, dyb, prize_x, prize_y = (int(x) for x in m)
        o = Optimize()
        o.add(a >= 0, b >= 0, dxa * a + dxb * b == prize_x + offset, dya * a + dyb * b == prize_y + offset)
        o.check()
        if m := o.model():
            res += m.evaluate(3 * a + b).as_long()
    return res


puzzle.answer_a, puzzle.answer_b = solve(0), solve(10_000_000_000_000)
