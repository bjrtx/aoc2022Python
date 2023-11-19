from aocd.models import Puzzle

puzzle = Puzzle(2022, 3)
data = puzzle.input_data.splitlines()

rucksacks = [
    (line[:len(line) // 2], line[len(line) // 2:]) for line in data
]
items = [set(l).intersection(r).pop() for l, r in rucksacks]

groups = [data[i: i + 3] for i in range(0, len(data), 3)]
badges = [set(a).intersection(b).intersection(c).pop() for a, b, c in groups]

def priority(item: str):
    return ord(item) + (1 - ord('a') if item.islower() else 27 - ord('A'))


puzzle.answer_a = sum(priority(item) for item in items)
puzzle.answer_b = sum(priority(item) for item in badges)