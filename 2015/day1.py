from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=1)
data = puzzle.input_data.strip()

puzzle.answer_a = 2 * data.count('(') - len(data)

pos = 0
for i, c in enumerate(data, start=1):
    pos += 1 if c == '(' else -1
    if pos == -1:
        break
puzzle.answer_b = i
