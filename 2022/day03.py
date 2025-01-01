import itertools

from aocd.models import Puzzle

puzzle = Puzzle(2022, 3)
data = puzzle.input_data.splitlines()

rucksacks = [
    (line[:len(line) // 2], line[len(line) // 2:]) for line in data
]
items = [set(left).intersection(right).pop() for left, right in rucksacks]
badges = [set(a).intersection(b).intersection(c).pop() for a, b, c in itertools.batched(data, 3)]


def priority(item: str):
    return ord(item) + (1 - ord('a') if item.islower() else 27 - ord('A'))


puzzle.answer_a = sum(priority(item) for item in items)
puzzle.answer_b = sum(priority(item) for item in badges)
