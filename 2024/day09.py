import itertools
import math
from collections import deque

import more_itertools
import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=9)
data = [int(d) for d in puzzle.input_data]


q = deque(itertools.chain.from_iterable([i] * n for i, n in enumerate(data[::2])))
q2 = q.copy()

res = j = 0
for i, n in enumerate(data):
    if not q:
        break
    for _ in range(n):
        if not q:
            break
        res += j * (q.pop() if i % 2 else q.popleft())
        j += 1
puzzle.answer_a = res

rle = []
q = q2
myq = deque(enumerate(data[::2]))
free = iter(data[1::2])
while myq:
    i, d = myq.popleft()
    rle.append((i, d))
    f = next(free, 0)
    while f:
        j, d = next(((jj, dd) for (jj, dd) in reversed(myq) if jj and dd <= f), (-1, -1))
        if d == -1:
            break
        else:
            f -= d
            k = myq.index((j, d))
            myq[k] = (0, d)
            rle.append((j, d))
    rle.append((0, f))

puzzle.answer_b = (sum(
    i * x for i, x in enumerate(more_itertools.run_length.decode(new_q))
))
