from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=3)


def houses(s):
    x, y = 0, 0
    seen = {(0, 0)}
    for char in s:
        match char:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        seen.add((x, y))
    return seen


puzzle.answer_a = len(houses(puzzle.input_data))
puzzle.answer_b = len(houses(puzzle.input_data[::2]) | houses(puzzle.input_data[1::2]))
