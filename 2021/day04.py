import copy
from collections import defaultdict

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=4)
data = puzzle.input_data.split('\n\n')

order = eval(data[0])

boards = [
    np.fromstring(elt, dtype=np.ubyte, sep=' ').reshape((5, 5))
    for elt in data[1:]
]

pos = defaultdict(list)
for b, board in enumerate(boards):
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            pos[x].append((b, i, j))


def winning_boards():
    seen = set()
    won = set()
    for elt in order:
        seen.add(elt)
        for b, i, j in pos[elt]:
            if b not in won:
                board = boards[b]
                if seen.issuperset(board[i, :]) or seen.issuperset(board[:, j]):
                    won.add(b)
                    yield board, elt, copy.deepcopy(seen)


first_win, elt, seen = more_itertools.first(winning_boards())
puzzle.answer_a = elt * sum(int(x) if int(x) not in seen else 0 for x in np.nditer(first_win))
last_win, elt, seen = more_itertools.last(winning_boards())
puzzle.answer_b = elt * sum(int(x) if int(x) not in seen else 0 for x in np.nditer(last_win))
