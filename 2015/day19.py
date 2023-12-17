from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=19)
data = puzzle.input_data.splitlines()

start = data[-1]
grammar = [
    (l, r)
    for l, _, r in (line.partition(' => ') for line in data[:-2])
]
d = defaultdict(list)
for l, r in grammar:
    d[l].append(r)


def step(string: str):
    for l, v in d.items():
        for i in range(len(string)):
            if string.startswith(l, i):
                yield from (string[:i] + r + string[i + len(l):] for r in v)


puzzle.answer_a = len(set(step(start)))
