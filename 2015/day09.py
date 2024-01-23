import itertools
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=9)
data = puzzle.input_data.splitlines()

distances = (
    re.fullmatch(r"(\w+) to (\w+) = (\d+)", line).groups()
    for line in data
)
distance_dict = {}
cities = set()
for a, b, d in distances:
    cities.add(a)
    cities.add(b)
    distance_dict[(a, b)] = distance_dict[(b, a)] = int(d)


def cost(permutation):
    return sum(distance_dict[p] for p in itertools.pairwise(permutation))


puzzle.answer_a = min(cost(p) for p in itertools.permutations(cities))
puzzle.answer_b = max(cost(p) for p in itertools.permutations(cities))
