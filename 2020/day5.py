from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=5)
data = puzzle.input_data.splitlines()

table = str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})

seats = {int(seat.translate(table), 2) for seat in data}

puzzle.answer_a = max(seats)
puzzle.answer_b = min(s for s in seats if s + 1 not in seats) + 1
