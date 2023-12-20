import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=13)
patterns = [s.splitlines() for s in puzzle.input_data.split('\n\n')]


def proper_match(la, lb):
    return more_itertools.iequals(zip(la, lb), zip(lb, la))


def count(test=proper_match):

    return sum(
        weight * sum(
            i
            for i in range(1, len(direction))
            if test(list(reversed(direction[:i])), direction[i:])
        )
        for pattern in patterns
        for (direction, weight) in ((list(more_itertools.transpose(pattern)), 1), (pattern, 100))
    )


puzzle.answer_a = count()


def smudge_match(la, lb):
    la, lb = list(la), list(lb)
    if la and lb:
        diff = sum(a != b for a, b in zip(la[0], lb[0]))
        return diff == 1 and proper_match(la[1:], lb[1:]) or diff == 0 and smudge_match(la[1:], lb[1:])
    else:
        return bool(la or lb)


puzzle.answer_b = count(test=lambda la, lb: smudge_match(la, lb) and not proper_match(la, lb))
