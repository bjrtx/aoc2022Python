import functools
import itertools

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=5)
data = puzzle.input_data

seeds = [int(s) for s in data.partition('\n')[0].partition(":")[-1].split()]

maps = list()
for line in data.splitlines()[1:]:
    if line.endswith('map:'):
        maps.append([])
    elif line:
        destination, source, range_ = map(int, line.split())
        maps[-1].append((source, destination, range_))


def apply_map(value, m):
    for source, destination, range_ in m:
        if source <= value < source + range_:
            return destination - source + value
    else:
        return value


def reverse_map(value, m):
    for source, destination, range_ in m:
        if destination <= value <= destination + range_:
            return source - destination + value
    else:
        return value


def translate(seed):
    return functools.reduce(apply_map, maps, seed)


intervals = sorted([(a, a + b) for a, b in more_itertools.batched(seeds, 2)])


def is_relevant(x):
    return any(a <= x < b for a, b in intervals)


notable = set(itertools.chain.from_iterable(intervals))
for i, m in enumerate(maps):
    endpoints = list(
        itertools.chain.from_iterable((source, source + range_) for source, _, range_ in m)
    )
    endpoints = [functools.reduce(reverse_map, reversed(maps[:i]), d) for d in endpoints]
    notable.update(filter(is_relevant, endpoints))

puzzle.answer_a = min(translate(seed) for seed in seeds)
puzzle.answer_b = min(translate(seed) for seed in notable)
