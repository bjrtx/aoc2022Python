import math
from collections import defaultdict
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=19)
data = puzzle.input_data.splitlines()

start = data[-1]
grammar = [
    (left, right)
    for left, _, right in (line.partition(' => ') for line in data[:-2])
]
rules, predecessors = defaultdict(list), defaultdict(list)
for left, right in grammar:
    rules[left].append(right)
    predecessors[right].append(left)


@cache
def step(string: str):
    s = set()
    for left, v in rules.items():
        for i in range(len(string)):
            if string.startswith(left, i):
                s |= set(string[:i] + r + string[i + len(left):] for r in v)
    return s


@cache
def step_back(string: str):
    s = set()
    for left, v in predecessors.items():
        for i in range(len(string)):
            if string.startswith(left, i):
                s |= set(string[:i] + r + string[i + len(left):] for r in v)
    return s


@cache
def age(string: str):
    print(string)
    if string == 'e':
        return 0
    else:
        return min((age(s) for s in step_back(string)), default=math.inf)


puzzle.answer_a = len(step(start))
res = 0
while start != 'e':
    for left, right in grammar:
        res += start.count(right)
        start = start.replace(right, left)
puzzle.answer_b = res
