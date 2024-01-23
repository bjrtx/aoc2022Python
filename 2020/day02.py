import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=2)
data = puzzle.input_data.splitlines()

res = 0
for line in data:
    min_, max_, letter, password = re.fullmatch(r'(\d+)-(\d+) ([a-z]): ([a-z]*)', line).groups()
    res += int(min_) <= password.count(letter) <= int(max_)

puzzle.answer_a = res

res = 0
for line in data:
    min_, max_, letter, password = re.fullmatch(r'(\d+)-(\d+) ([a-z]): ([a-z]*)', line).groups()
    res += (password[int(min_) - 1] == letter) ^ (password[int(max_) - 1] == letter)

puzzle.answer_b = res
