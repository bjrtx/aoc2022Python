import graphlib
from collections import defaultdict

import more_itertools
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=5)
rules, updates = puzzle.input_data.split('\n\n')

rules = [(s[:2], s[3:]) for s in rules.splitlines()]
updates = [t.split(',') for t in updates.splitlines()]
reqs = defaultdict(set)
for a, b in rules:
    reqs[b].add(a)


def is_correct(u):
    seen = set()
    for x in reversed(u):
        if seen & reqs[x]:
            return False
        seen.add(x)
    else:
        return True


def correct(u):
    u = set(u)
    ts = graphlib.TopologicalSorter({x: u & reqs[x] for x in u})
    return tuple(ts.static_order())


incorrect_updates, correct_updates = more_itertools.partition(is_correct, updates)
puzzle.answer_a = sum(int(u[(len(u) // 2)]) for u in correct_updates)
puzzle.answer_b = sum(int(correct(u)[(len(u) // 2)]) for u in incorrect_updates)
