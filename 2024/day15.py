import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=15)
data = puzzle.input_data

warehouse, moves = data.split('\n\n')
warehouse = np.array([list(row) for row in warehouse.splitlines()])
m, n = warehouse.shape


def step_(i, j, dir_):
    match dir_:
        case '^':
            dir_ = (-1, 0)
        case 'v':
            dir_ = (1, 0)
        case '>':
            dir_ = (0, 1)
        case '<':
            dir_ = (0, -1)
    stack = [[(i, j)]]
    while True:
        positions = stack[-1]
        if all(warehouse[*pos] == '.' for pos in positions):
            break

        new_positions = {
            tuple(np.array(dir_) + t)
            for t in positions if warehouse[t] != '.'}
        if any(warehouse[pos] == '#' for pos in new_positions):
            return
        new_positions = {t for t in new_positions if warehouse[t] != '.'}
        if dir_[0]:
            new_positions |= {
                (x, y + e) for x, y in new_positions for (c, e) in [(']', -1), ('[', 1)] if warehouse[x, y] == c
            }
        stack.append(new_positions)

    for new in reversed(stack[:-1]):
        for pos in new:
            warehouse[tuple(pos + np.array(dir_))], warehouse[pos] = warehouse[pos], '.'
    warehouse[stack[0][0]] = '.'


def run():
    for d in moves:
        if d != '\n':
            [(i, j)] = np.argwhere(warehouse == '@')
            step_(i, j, d)
    return str(sum(100 * i + j for i, j in np.argwhere((warehouse == 'O') + (warehouse == '['))))


puzzle.answer_a = run()

warehouse, moves = data.split('\n\n')
warehouse = np.array([list(row) for row in warehouse.splitlines()])
ddata = np.zeros(shape=(m, 2 * n), dtype=np.str_)
for i in range(m):
    for j in range(n):
        match warehouse[i, j]:
            case '.':
                ddata[i, 2 * j: 2 * j + 2] = '..'
            case 'O':
                ddata[i, 2 * j: 2 * j + 2] = '[', ']'
            case '#':
                ddata[i, 2 * j: 2 * j + 2] = '#'
            case '@':
                ddata[i, 2 * j: 2 * j + 2] = '@', '.'

warehouse = ddata
puzzle.answer_b = run()
