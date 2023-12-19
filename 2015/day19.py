from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=19)
data = puzzle.input_data.splitlines()

start = data[-1]
grammar = [
    (left, right)
    for left, _, right in (line.partition(' => ') for line in data[:-2])
]
d = defaultdict(list)
for left, right in grammar:
    d[left].append(right)


def step(string: str):
    for left, v in d.items():
        for i in range(len(string)):
            if string.startswith(left, i):
                yield from (string[:i] + r + string[i + len(left):] for r in v)


puzzle.answer_a = len(set(step(start)))
