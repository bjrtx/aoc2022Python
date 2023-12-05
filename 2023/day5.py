import functools
import itertools

import more_itertools

import tqdm
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=5)
data = puzzle.input_data

seeds = [int(s) for s in data.partition('\n')[0].partition(":")[-1].split()]

maps = list()
for line in data.splitlines()[1:]:
    if line.endswith('map:'):
        curr_map = []
        maps.append(curr_map)
    elif line:
        dest, source, range_ = map(int, line.split())
        curr_map.append((source, dest, range_))


def translate(seed):
    return functools.reduce(lambda s, m: apply_map(m, s), maps, seed)


def apply_map(m, value):
    for source, dest, range_ in m:
        if source <= value < source + range_:
            return dest - source + value
    else:
        return value


def reverse_map(m, value):
    for source, dest, range_ in m:
        if dest <= value <= dest + range_:
            return source - dest + value
    else:
        return value


intervals = sorted([(a, a + b) for a, b in more_itertools.batched(seeds, 2)])


def is_relevant(x):
    return any(a <= x < b for a, b in intervals)


notable = set(itertools.chain.from_iterable(intervals))
for i, m in enumerate(maps):
    endpoints = list(
        itertools.chain.from_iterable((source, source + range_) for source, _, range_ in m)
    )
    for mm in reversed(maps[:i]):
        endpoints = [reverse_map(mm, d) for d in endpoints]
    notable.update(filter(is_relevant, endpoints))

puzzle.answer_a = min(translate(seed) for seed in seeds)
puzzle.answer_b = min(translate(seed) for seed in notable)
