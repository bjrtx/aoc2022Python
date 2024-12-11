from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=11)
data = puzzle.input_data.split()


@cache
def blink(stone, k):
    if k == 0:
        return 1
    elif stone == '0':
        return blink('1', k - 1)
    elif len(stone) % 2 == 0:
        m = len(stone) // 2
        return blink(stone[:m], k - 1) + blink(str(int(stone[-m:])), k - 1)
    else:
        return blink(str(int(stone) * 2024), k - 1)


puzzle.answer_a, puzzle.answer_b = (sum(blink(stone, n) for stone in data) for n in (25, 75))