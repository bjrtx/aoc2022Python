import operator
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=7)
data = puzzle.input_data.splitlines()
assignments = ([s.strip() for s in line.split("->")] for line in data)
expressions = {var: left_hand for left_hand, var in assignments}


@cache
def evaluate(expr: str):
    operations = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift
    }
    match expr.split():
        case [left, ("AND" | "OR" | "LSHIFT" | "RSHIFT") as op, right]:
            return operations[op](evaluate(left), evaluate(right))
        case ["NOT", arg]:
            return ~evaluate(arg)
        case [value] if value.isnumeric():
            return int(value)
        case [variable]:
            return evaluate(expressions[variable])


puzzle.answer_a = evaluate('a')
expressions['b'] = puzzle.answer_a
evaluate.cache_clear()
puzzle.answer_b = evaluate('a')
