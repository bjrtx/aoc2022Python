import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=1)
data = [eval(x) for x in puzzle.input_data.splitlines()]

puzzle.answer_a = sum(data)
seen = set()
for f in itertools.accumulate(itertools.cycle(data), initial=0):
    if f in seen:
        puzzle.answer_b = f
        break
    seen.add(f)
