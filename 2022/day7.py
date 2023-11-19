from collections import defaultdict
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(2022, 7)
data = puzzle.input_data.splitlines()


class Directory:
    def __init__(self):
        self.direct_files = 0
        self.subdirectories = defaultdict(self._child)
        self.parent = None

    def _child(self):
        d = Directory()
        d.parent = self
        return d


root = Directory()
wdir = root
for line in data:
    if line == "$ cd /":
        wdir = root
    elif line == "$ cd ..":
        if wdir != root:
            wdir = wdir.parent
    elif line.startswith("$ cd"):
        name = line.split()[-1]
        wdir = wdir.subdirectories[name]
    elif not (line.startswith("$") or line.startswith("dir")):
        value = int(line.split(maxsplit=1)[0])
        wdir.direct_files += value


@cache
def weight(directory):
    return directory.direct_files + sum(weight(d) for d in directory.subdirectories.values())


def all_directories(start=root):
    yield start
    for d in start.subdirectories.values():
        yield from all_directories(start=d)


weights = [weight(d) for d in all_directories()]
puzzle.answer_a = sum(w for w in weights if w <= 100_000)

needed_space = 30_000_000 - 70_000_000 + weight(root)
puzzle.answer_b = min(w for w in weights if w >= needed_space)
