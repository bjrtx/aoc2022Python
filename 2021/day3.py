import copy

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
data = puzzle.input_data.splitlines()

c = [0 for _ in data[0]]
for s in data:
    for i, x in enumerate(s):
        if x == '1':
            c[i] += 1

most_common_bits = ['1' if 2 * v >= len(data) else '0' for v in c]
not_bits = ['0' if c == '1' else '1' for c in most_common_bits]
gamma_rate = int(''.join(most_common_bits), 2)
epsilon_rate = int(''.join(not_bits), 2)
puzzle.answer_a = gamma_rate * epsilon_rate
