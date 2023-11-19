import itertools
from typing import Iterable

from aocd.models import Puzzle

puzzle = Puzzle(2022, 8)
data = puzzle.input_data

tree_matrix = [[(int(c), (i, j)) for j, c in enumerate(line)] for i, line in enumerate(data.splitlines())]
m = len(tree_matrix)
n = len(tree_matrix[0])
columns = [[tree_matrix[i][j] for i in range(m)] for j in range(n)]
sight_lines = itertools.chain(
    tree_matrix,
    (list(reversed(line)) for line in tree_matrix),
    columns,
    (list(reversed(column)) for column in columns)
)
visible = set()
for sight_line in sight_lines:
    tallest = -1
    for (h, coords) in sight_line:
        if h > tallest:
            tallest = h
            visible.add(coords)

puzzle.answer_a = len(visible)


def left_visibility(line: Iterable[int]):
    stack = []
    res = []
    for i, x in enumerate(line):
        while stack and stack[-1][1] < x:
            stack.pop()
        index = stack[-1][0] if stack else 0
        res.append(i - index)
        stack.append((i, x))
    return res


def horizontal_score(line):
    return [a * b for a, b in zip(left_visibility(line), reversed(left_visibility(reversed(line))))]


lines = [[x for x, _ in line] for line in tree_matrix]
columns = [[x for x, _ in column] for column in columns]
line_score = [horizontal_score(line) for line in lines]
column_score = [horizontal_score(column) for column in columns]
puzzle.answer_b = max(line_score[i][j] * column_score[j][i] for i in range(m) for j in range(n))
