import functools
import itertools
import operator

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=10)
data = puzzle.input_data


def reverse(list_, n, pos):
    tmp = list_[pos: pos + n]
    a, b = len(tmp), n - len(tmp)
    b = n - len(tmp)
    tmp += list_[:b]
    tmp.reverse()
    list_[pos: pos + a] = tmp[:a]
    list_[: b] = tmp[a:]


def aux(lengths, list_, pos=0, skip=0):
    for length in lengths:
        reverse(list_, length, pos)
        pos = (pos + length + skip) % len(list_)
        skip += 1
    return list_, pos, skip


h, _, _ = aux(eval(data), list(range(256)))
puzzle.answer_a = h[0] * h[1]


def knot_hash(input_: str):
    input_ = [ord(c) for c in input_] + [17, 31, 73, 47, 23]
    pos = skip = 0
    list_ = list(range(256))
    for _ in range(64):
        list_, pos, skip = aux(input_, list_, pos, skip)
    dense = [
        functools.reduce(operator.xor, batch)
        for batch in itertools.batched(list_, 16)
    ]
    return ''.join(f'{d:0{2}x}' for d in dense)


puzzle.answer_b = knot_hash(data.strip())