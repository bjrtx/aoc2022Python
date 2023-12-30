from collections import Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=9)
data = [int(x) for x in puzzle.input_data.splitlines()]


c = Counter(data[:25])
for a, b in zip(data[25:], data):
    if not any(2 * k != a and (a - k) in c for k in c):
        break
    c[a] += 1
    c[b] -= 1
    c = +c

puzzle.answer_a = a

i = j = total = 0
while total != a:
    while total < a:
        total += data[j]
        j += 1
    while total > a:
        total -= data[i]
        i += 1
puzzle.answer_b = min(data[i:j]) + max(data[i:j])
