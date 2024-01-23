import itertools

from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(2022, 9)
data = puzzle.input_data.splitlines()
instructions = [(w[0], int(w[1])) for w in [line.split() for line in data]]


class Rope:
    def __init__(self, length):
        self.length = length
        self.nodes = [np.zeros(2) for _ in range(self.length)]
        self.memory = {(0, 0)}

    def update(self):
        for i, (a, b) in enumerate(itertools.pairwise(self.nodes)):
            diff = a - b
            if np.any(np.abs(diff) > 1):
                self.nodes[i + 1] += np.sign(diff)
        self.memory.add(tuple(self.nodes[-1]))

    def follow_instructions(self):
        for d, n in instructions:
            for _ in range(n):
                if d == 'D':
                    self.nodes[0][1] -= 1
                elif d == 'U':
                    self.nodes[0][1] += 1
                elif d == 'L':
                    self.nodes[0][0] -= 1
                elif d == 'R':
                    self.nodes[0][0] += 1
                self.update()

    @staticmethod
    def solve(length=2):
        r = Rope(length)
        r.follow_instructions()
        return len(r.memory)


puzzle.answer_a, puzzle.answer_b = Rope.solve(), Rope.solve(10)
