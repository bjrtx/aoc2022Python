import itertools
import operator
import re
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=9)
data = puzzle.input_data.splitlines()

matches = (
    re.fullmatch(r"(\w+) to (\w+) = (\d+)", line)
    for line in data
)
distances = (m.groups() for m in matches)
distance_dict = {}
cities = set()
for a, b, d in distances:
    cities.add(a)
    cities.add(b)
    distance_dict[(a, b)] = distance_dict[(b, a)] = int(d)
print(distance_dict)
puzzle.answer_a = min(
    sum(
        distance_dict[p]
        for p in itertools.pairwise(permutation)
    )
    for permutation in itertools.permutations(cities)
)
puzzle.answer_b = max(
    sum(
        distance_dict[p]
        for p in itertools.pairwise(permutation)
    )
    for permutation in itertools.permutations(cities)
)
