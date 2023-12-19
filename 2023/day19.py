import copy
import math
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=19)
workflows, ratings = [part.splitlines() for part in puzzle.input_data.split('\n\n')]
conditions = {
    name: cond.split(',')
    for name, cond in (re.match(r'(\w+)\{(.*)}', w).groups() for w in workflows)
}


class Box:
    def __init__(self):
        self.ranges = {k: range(1, 4001) for k in 'xmas'}

    def __contains__(self, state):
        return all(state[k] in r for k, r in self.ranges.items())

    def __len__(self):
        return math.prod(len(r) for r in self.ranges.values())

    def bisect(self, key, value):
        (a, b), r = (copy.deepcopy(self) for _ in range(2)), self.ranges[key]
        a.ranges[key] = range(r.start, min(value, r.stop))
        b.ranges[key] = range(max(value, r.start), r.stop)
        return a, b


def disjoint_boxes(state='in', box=Box()):
    if state == 'A':
        if box:
            yield box
    elif state != 'R':
        for cond in conditions[state]:
            match re.split('([:><])', cond):
                case [var, '>', t, ':', next_]:
                    box, nbox = box.bisect(var, int(t) + 1)
                case [var, '<', t, ':', next_]:
                    nbox, box = box.bisect(var, int(t))
                case _:
                    nbox, next_ = box, cond
            yield from disjoint_boxes(next_, nbox)


boxes = list(disjoint_boxes())
ratings = (eval(f"dict({r[1:-1]})") for r in ratings)
puzzle.answer_a = sum((sum(r.values()) for r in ratings if any(r in b for b in boxes)))
puzzle.answer_b = sum(len(i) for i in boxes)
