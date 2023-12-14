import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=14)
data = puzzle.input_data.splitlines()


def roll_up(col):
    return list(
        itertools.chain.from_iterable(
            sorted(g, reverse=True)
            for k, g in itertools.groupby(col, key=lambda x: x != '#')
        )
    )


def transpose(matrix):
    return list(zip(*matrix))


def cycle(matrix):
    # N
    ndata = transpose(list(map(roll_up, transpose(matrix))))
    # W
    ndata = list(map(roll_up, ndata))
    # S
    columns = list(map(roll_up, transpose(reversed(ndata))))
    ndata = list(reversed(transpose(columns)))
    # E
    ndata = list(map(roll_up, map(reversed, ndata)))
    ndata = [list(reversed(row)) for row in ndata]
    return ndata


def total_weight(matrix):
    return sum(i for col in transpose(matrix) for i, x in enumerate(reversed(col), 1) if x == 'O')


puzzle.answer_a = total_weight(transpose(list(map(roll_up, transpose(data)))))

temp = data
mem = dict()
step = 0
bound = 1_000_000_000
while (step := step + 1) <= bound:
    string = repr(temp)
    if string in mem:
        bound = step + (bound - step) % (step - mem[string])
    else:
        mem[string] = step
    temp = cycle(temp)

puzzle.answer_b = total_weight(temp)
