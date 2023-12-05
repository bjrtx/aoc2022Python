import functools
import itertools
from collections import Counter, deque

import more_itertools
import numpy as np

import tqdm
from aocd.models import Puzzle
from numpy.linalg import matrix_power

puzzle = Puzzle(year=2021, day=6)
data = eval(puzzle.input_data)

mat = np.zeros((9,9), dtype=np.longlong)
for age in range(8):
    mat[age, age+1] = 1
mat[6, 0] = mat[8, 0] = 1

fish = np.array([data.count(i) for i in range(9)])
puzzle.answer_a = np.sum(matrix_power(mat, 80) @ fish)
puzzle.answer_b = np.sum(matrix_power(mat, 256) @ fish)
