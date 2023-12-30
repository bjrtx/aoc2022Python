import re
from functools import cache

import networkx
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=7)
data = puzzle.input_data.splitlines()


d = networkx.DiGraph()
for line in data:
    left, _, right = line.partition(' bags contain ')
    for num, col in re.findall(r'(\d+) (\w+ \w+) bag', right):
        d.add_edge(left, col, cost=int(num))

puzzle.answer_a = len(networkx.ancestors(d, "shiny gold"))


@cache
def cost(col):
    return 1 + sum(w["cost"] * cost(n) for n, w in d[col].items())


puzzle.answer_b = cost("shiny gold") - 1
