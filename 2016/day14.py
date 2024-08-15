import hashlib
import itertools
import re

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=14)
data = puzzle.input_data


def multiples():
    hashes = (
        hashlib.md5((data + str(i)).encode()).hexdigest() for i in itertools.count()
    )
    triples = re.compile(r'(.)\1\1')
    fives = re.compile(r'(.)\1\1')
    for h in hashes:
        m = triples.search(h)
        if m:
            f = fives.findall(h)
            yield m[0], f
        else:
            yield None, []

d = {}
for i, (_, f) in enumerate(more_itertools.take(1_000, multiples())):
    for v in f:
        d[v] = i
for i, ((t, _), (_, f)) in enumerate(zip(multiples(), itertools.islice(multiples(), 1_000, None))):
    for v in f:
        d[v] = i + 1_000
    print(i)
    if t is not None and d.get(t, -1) > i:
        print(t)
