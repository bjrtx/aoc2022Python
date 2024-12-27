from aocd.models import Puzzle
from more_itertools import one

puzzle = Puzzle(year=2021, day=3)
data = puzzle.input_data.splitlines()

c = [t.count('1') for t in zip(*data)]

gamma_rate = 0
for v in c:
    gamma_rate = (gamma_rate << 1) | (2 * v >= len(data))
epsilon_rate = gamma_rate ^ ((1 << len(data[0])) - 1)
puzzle.answer_a = gamma_rate * epsilon_rate

oxygen_candidates = data[:]
co2_candidates = data[:]
for i in range(len(data[0])):
    if len(oxygen_candidates) == 1:
        break
    most_common = 2 * sum(x[i] == '1' for x in oxygen_candidates) >= len(oxygen_candidates)
    oxygen_candidates = [x for x in oxygen_candidates if x[i] == '01'[most_common]]
for i in range(len(data[0])):
    if len(co2_candidates) == 1:
        break
    least_common = 2 * sum(x[i] == '0' for x in co2_candidates) > len(co2_candidates)
    co2_candidates = [x for x in co2_candidates if x[i] == '01'[least_common]]
puzzle.answer_b = int(one(oxygen_candidates), 2) * int(one(co2_candidates), 2)
