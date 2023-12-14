import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=13)
patterns = [s.splitlines() for s in puzzle.input_data.split('\n\n')]


def proper_match(la, lb):
    return more_itertools.iequals(zip(la, lb), zip(lb, la))


def count(f=proper_match):
    res = 0
    for pattern in patterns:
        columns = list(zip(*pattern))
        for n, (direction, weight) in enumerate(((columns, 1), (pattern, 100))):
            for i in range(1, len(direction)):
                la, lb = map(list, (reversed(direction[:i]), direction[i:]))
                if f(la, lb):
                    res += i * weight
    return res


puzzle.answer_a = count()


def smudge_match(la, lb):
    la = list(la)
    lb = list(lb)
    if la and lb:
        diff = sum(a != b for a, b in zip(la[0], lb[0]))
        return diff == 1 and proper_match(la[1:], lb[1:]) or diff == 0 and smudge_match(la[1:], lb[1:])
    else:
        return bool(la or lb)


puzzle.answer_b = count(f=lambda la, lb: smudge_match(la, lb) and not proper_match(la, lb))
