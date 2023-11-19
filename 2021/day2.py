from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
data = puzzle.input_data.splitlines()
data = [line.split() for line in data]
data = [(t[0], int(t[1])) for t in data]

horizontal = 0
depth = 0
for cmd, v in data:
    match cmd:
        case "forward":
            horizontal += v
        case "down":
            depth += v
        case "up":
            depth -= v

puzzle.answer_a = horizontal * depth

horizontal = 0
depth = 0
aim = 0
for cmd, v in data:
    match cmd:
        case "forward":
            horizontal += v
            depth += aim * v
        case "down":
            aim += v
        case "up":
            aim -= v

puzzle.answer_b = horizontal * depth
