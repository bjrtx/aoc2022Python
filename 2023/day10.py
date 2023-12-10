import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)
data = puzzle.input_data.splitlines()

start = next((i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == 'S')


def neighbours(p):
    i, j = p
    match data[i][j]:
        case '|':
            return (i - 1, j), (i + 1, j)
        case '-':
            return (i, j - 1), (i, j + 1)
        case 'L':
            return (i - 1, j), (i, j + 1)
        case 'J':
            return (i - 1, j), (i, j - 1)
        case '7':
            return (i, j - 1), (i + 1, j)
        case 'F':
            return (i + 1, j), (i, j + 1)
        case 'S':
            return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        case _:
            return ()


def points():
    prev, curr = None, start
    yield curr
    while True:
        prev, curr = curr, (set(neighbours(curr)) - {prev}).pop()
        if curr == start:
            break
        yield curr


v = list(points())

#  maths!
puzzle.answer_a = len(v) // 2
v_off = itertools.islice(itertools.cycle(v), 1, None)
double_area = abs(sum(b * c - a * d for (a, b), (c, d) in zip(v, v_off)))
puzzle.answer_b = (double_area - len(v)) // 2 + 1
