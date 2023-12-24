import itertools
import re
from collections import defaultdict, Counter
from functools import cache
from pprint import pprint

import numpy
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=24)
data = puzzle.input_data.splitlines()

hailstones = [[eval(t) for t in line.split('@')] for line in data]

smallest, largest = 200000000000000, 400000000000000

# Okay, I still need to write this one properly


def intersect(la, lb):
    (xa, ya, _), (vxa, vya, _) = la
    (xb, yb, _), (vxb, vyb, _) = lb
    return (
            (det := vxb * vya - vxa * vyb) != 0
            and (ta := (vxb * (yb - ya) - (xb - xa) * vyb) / det) >= 0
            and ((xa - xb) * vya + vxa * (yb - ya)) / det >= 0
            and smallest <= xa + ta * vxa <= largest
            and smallest <= ya + ta * vya <= largest
    )


puzzle.answer_a = sum(intersect(*p) for p in itertools.combinations(hailstones, 2))

(most_common, _), *_ = Counter(h[1][0] for h in hailstones).most_common(1)

for i, h in enumerate([h for h in hailstones if h[1][0] == most_common][:4]):
    (x, y, z), (a, b, c) = h
    def invert(val): return f'{-val}' if val >= 0 else f'+{abs(val)}'


    u1 = f'X{invert(x)}'
    u2 = f'Y{invert(y)}'
    u3 = f'Z{invert(z)}'
    v1 = f'A{invert(a)}'
    v2 = f'B{invert(b)}'
    v3 = f'C{invert(c)}'
    print(f'({u2}) * ({v3}) == ({u3}) * ({v2})', end=',\n')
    print(f'({u3}) * ({v1}) == ({u1}) * ({v3})', end=',\n')
    print(f'({u1}) * ({v2}) == ({u2}) * ({v1})', end=',\n')

"""sage
X,Y,Z,A,B,C = var('X Y Z A B C')
eqs = [
(Y-167088974969088)*(C-197)==(Z-180640699244168)*(B-172),
(Z-180640699244168)*(A+25)==(X-348161249618981)*(C-197),
(X-348161249618981)*(B-172)==(Y-167088974969088)*(A+25),
(Y-278549979949651)*(C+14)==(Z-271447667273247)*(B+15),
(Z-271447667273247)*(A+25)==(X-279513103505321)*(C+14),
(X-279513103505321)*(B+15)==(Y-278549979949651)*(A+25),
(Y-243445877015545)*(C+72)==(Z-243218965554108)*(B-107),
(Z-243218965554108)*(A+25)==(X-212482017498590)*(C+72),
(X-212482017498590)*(B-107)==(Y-243445877015545)*(A+25),
(Y-293712368542560)*(C-15)==(Z-301144076275114)*(B+26),
(Z-301144076275114)*(A+25)==(X-358073536352267)*(C-15),
(X-358073536352267)*(B+26)==(Y-293712368542560)*(A+25),
]
neqs = [
        (eqs[i] - eqs[j]) for i in range(3) for j in range(i + 3, 11, 3)
]
solve(neqs, [X,Y,Z,A,B,C])
"""
