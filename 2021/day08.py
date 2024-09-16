import re

import sympy.combinatorics
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
data = puzzle.input_data.splitlines()

digits = ('abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf',
          'abcdefg', 'abcdfg')
ddigits = {v: i for i, v in enumerate(digits)}


res_a = res_b = 0
for line in data:
    groups = sorted(
        word
        for word in re.split(r'[ |]', line)
        if word
    )

    perm = next(
        p for p in sympy.combinatorics.SymmetricGroup(7).elements
        if all(
            ''.join(sorted(chr(((ord(c) - ord('a')) ^ p) + ord('a')) for c in g)) in digits
            for g in groups
        )
    )

    _, _, output = line.partition(' | ')
    val = []
    for w in output.split():
        res_a += len(w) in (2, 3, 4, 7)
        val.append(ddigits[''.join(sorted(chr(((ord(c) - ord('a')) ^ perm) + ord('a')) for c in w))])
    res_b += val[0] * 1_000 + val[1] * 100 + val[2] * 10 + val[3]

puzzle.answer_a = res_a
puzzle.answer_b = res_b
