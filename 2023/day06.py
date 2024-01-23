from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=6)
data = puzzle.input_data.splitlines()

times = [int(x) for x in data[0].partition(":")[-1].split()]
distances = [int(x) for x in data[1].partition(":")[-1].split()]

res = 1
for t, d in zip(times, distances):
    minimum = min(s for s in range(t) if s * (t - s) >= d)
    maximum = max(s for s in range(t) if s * (t - s) >= d)
    res *= (maximum - minimum + 1)

puzzle.answer_a = res


time = int(''.join(data[0].partition(":")[-1].split()))
distance = int(''.join(data[1].partition(":")[-1].split()))

speed = (distance // time)
minimum = min(s for s in range(speed, time) if s * (time - s) >= distance)
maximum = max(s for s in range(speed, time) if s * (time - s) >= distance)

puzzle.answer_b = maximum - minimum + 1
