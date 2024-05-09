import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=7)
data = puzzle.input_data.splitlines()


def super_hyper_net(s):
    blocks = re.split(r'\W', s)
    return blocks[::2], blocks[1::2]


puzzle.answer_a = sum(
    any(re.search(r'(\w)(?!\1)(\w)\2\1', block) for block in s)
    and not any(re.search(r'(\w)(?!\1)(\w)\2\1', block) for block in h)
    for s, h in (super_hyper_net(line) for line in data)
)


def matches(line):
    s, h = super_hyper_net(line)
    aba = {
        block[m.start():m.start() + 2]
        for block in s
        for m in re.finditer(r'(\w)(?=(?!\1)\w\1)', block)
    }
    bab = {
        block[m.start() + 1:m.start() + 3]
        for block in h
        for m in re.finditer(r'(\w)(?=(?!\1)\w\1)', block)
    }
    return not aba.isdisjoint(bab)


puzzle.answer_b = sum(matches(line) for line in data)
