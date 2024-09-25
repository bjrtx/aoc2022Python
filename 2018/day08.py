from collections import Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=8)

source = (int(x) for x in puzzle.input_data.split())


class Node:
    def __init__(self):
        nb_children = next(source)
        nb_metadata = next(source)
        self.children = [Node() for _ in range(nb_children)]
        self.metadata = [next(source) for _ in range(nb_metadata)]

    def check(self):
        return sum(self.metadata) + sum(n.check() for n in self.children)

    def value(self):
        if self.children:
            select = Counter(
                i - 1
                for i in self.metadata
                if 0 < i <= len(self.children))
            return sum(self.children[i].value() * v for i, v in select.items())
        else:
            return sum(self.metadata)


n = Node()
puzzle.answer_a, puzzle.answer_b = n.check(), n.value()
