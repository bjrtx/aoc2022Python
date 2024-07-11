import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=8)
data = puzzle.input_data.splitlines()


class Screen:
    def __init__(self):
        self.data = np.zeros((6, 50), dtype=np.bool)

    def parse(self, command):
        match command.split():
            case ['rect', size]:
                a, b = [int(x) for x in size.split('x')]
                self.data[:b, :a] = True
            case ['rotate', 'row', row, 'by', amount]:
                y = int(row[2:])
                self.data[y] = np.roll(self.data[y], int(amount))
            case ['rotate', 'column', column, 'by', amount]:
                x = int(column[2:])
                self.data[:, x] = np.roll(self.data[:, x], int(amount))


screen = Screen()
for command in data:
    screen.parse(command)
puzzle.answer_a = screen.data.sum()

for line in np.where(screen.data, '*', ' '):
    print(*line)
