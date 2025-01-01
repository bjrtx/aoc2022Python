import heapq
import itertools

from aocd.models import Puzzle

puzzle = Puzzle(2022, 1)
data = puzzle.input_data.splitlines()

calories = (
    sum(int(x) for x in g)
    for k, g in itertools.groupby(data, key=bool)
    if k
)
top_three = heapq.nlargest(3, calories)
puzzle.answer_a = top_three[0]
puzzle.answer_b = sum(top_three)
