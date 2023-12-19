from aocd.models import Puzzle

puzzle = Puzzle(2022, 9)
data = puzzle.input_data.splitlines()
instructions = [(w[0], int(w[1])) for w in [line.split() for line in data]]


class Rope:
    def __init__(self, length=2):
        self.length = length
        self.nodes = [[0, 0] for _ in range(self.length)]
        self.memory = {(0, 0)}

    @staticmethod
    def _sgn(a):
        return -1 if a <= -1 else 1 if a >= 1 else 0

    def update(self):
        for i in range(self.length - 1):
            diff = [a - b for a, b in zip(self.nodes[i], self.nodes[i + 1])]
            if max(abs(x) for x in diff) > 1:
                steps = [self._sgn(d) for d in diff]
                self.nodes[i + 1][0] += steps[0]
                self.nodes[i + 1][1] += steps[1]
        self.memory.add(tuple(self.nodes[-1]))

    def follow_instructions(self, instructions):
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


r = Rope()
r.follow_instructions(instructions)

puzzle.answer_a = len(r.memory)
r = Rope(10)
r.follow_instructions(instructions)
puzzle.answer_b = len(r.memory)
