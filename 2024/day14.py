import math
import re
import statistics

from matplotlib import pyplot as plt

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=14)
data = puzzle.input_data

robots = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", data)
quadrants = [0] * 4
for m in robots:
    px, py, vx, vy = [int(x) for x in m]
    x = (px + 100 * vx) % 101
    y = (py + 100 * vy) % 103
    if x != 50 and y != 51:
        quadrants[2 * (x < 50) + (y < 51)] += 1

puzzle.answer_a = math.prod(quadrants)

variances = []
for i in range(10_000):
    xs = []
    ys = []
    for m in robots:
        px, py, vx, vy = [int(x) for x in m]
        xs.append((px + i * vx) % 101)
        ys.append((py + i * vy) % 103)
    variances.append(statistics.pvariance(xs + ys, 0))

puzzle.answer_b = str(np.argmin(variances))
