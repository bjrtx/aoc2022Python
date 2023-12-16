import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=16)
data = puzzle.input_data.splitlines()


def new_directions(pos, direction):
    (x, y), (dx, dy) = pos, direction
    match data[x][y]:
        case '.':
            yield direction
        case '/':
            yield -dy, -dx
        case '\\':
            yield dy, dx
        case '|':
            if dy:
                yield -1, 0
                yield 1, 0
            else:
                yield direction
        case '-':
            if dx:
                yield 0, -1
                yield 0, 1
            else:
                yield direction


def neighbours(pos, direction):
    return {
        (p, d)
        for p, d in (((pos[0] + dx, pos[1] + dy), (dx, dy)) for dx, dy in new_directions(pos, direction))
        if 0 <= p[0] < m and 0 <= p[1] < n
    }


m, n = len(data), len(data[0])


def energized(start=(0, 0), direction=(0, 1)):
    mem = set()
    q = [(start, direction)]
    while q:
        curr = q.pop()
        mem.add(curr)
        q += neighbours(*curr) - mem
    return len({pos for pos, _ in mem})


puzzle.answer_a = energized()

possible = itertools.chain(
    [((0, j), (1, 0)) for j in range(n)],
    [((m - 1, j), (-1, 0)) for j in range(n)],
    [((i, 0), (0, 1)) for i in range(m)],
    [((i, n - 1), (0, -1)) for i in range(m)]
)
puzzle.answer_b = max(itertools.starmap(energized, possible))
