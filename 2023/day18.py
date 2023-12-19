import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=18)
data = puzzle.input_data.splitlines()


def solve(instructions):
    x, y = (0, 0)
    visited = [(x, y)]
    for d, n in instructions:
        match d:
            case 'R':
                y += n
            case 'L':
                y -= n
            case 'D':
                x += n
            case 'U':
                x -= n
        visited.append((x, y))

    v_off = itertools.islice(itertools.cycle(visited), 1, None)
    double_area = sum(b*c - a*d for (a, b), (c, d) in zip(visited, v_off))
    return abs(double_area) // 2 + sum(n for _, n in instructions) // 2 + 1


instructions_a = [(d, int(n)) for d, n, _ in (line.split() for line in data)]

puzzle.answer_a = solve(instructions_a)

instructions_b = [
    ('RDLU'[int(code[-1])], int(code[:-1], 16))
    for code in (line.rpartition(' ')[-1][2:-1] for line in data)
]

puzzle.answer_b = solve(instructions_b)
