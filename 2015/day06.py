import numpy as np

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=6)
data = puzzle.input_data.splitlines()


def rectangle(a: str, b: str):
    xa, ya = eval(a)
    xb, yb = eval(b)
    xa, xb = sorted([xa, xb])
    ya, yb = sorted([ya, yb])
    return xa, xb + 1, ya, yb + 1


def first_task():
    lights = np.zeros((1000, 1000), dtype=np.bool_)
    for instruction in data:
        match instruction.split():
            case ["turn", on_off, a, "through", b]:
                xa, xb, ya, yb = rectangle(a, b)
                lights[xa:xb, ya:yb] = on_off == "on"
            case ["toggle", a, "through", b]:
                xa, xb, ya, yb = rectangle(a, b)
                lights[xa:xb, ya:yb] = np.logical_not(lights[xa:xb, ya:yb])
    return lights.sum()


def second_task():
    lights = np.zeros((1000, 1000), dtype=np.int_)
    for instruction in data:
        match instruction.split():
            case ["turn", "on", a, "through", b]:
                xa, xb, ya, yb = rectangle(a, b)
                lights[xa:xb, ya:yb] += 1
            case ["turn", "off", a, "through", b]:
                xa, xb, ya, yb = rectangle(a, b)
                lights[xa:xb, ya:yb] = np.maximum(lights[xa:xb, ya:yb] - 1, 0)
            case ["toggle", a, "through", b]:
                xa, xb, ya, yb = rectangle(a, b)
                lights[xa:xb, ya:yb] += 2
    return lights.sum()


puzzle.answer_a = first_task()
puzzle.answer_b = second_task()
