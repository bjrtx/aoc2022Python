from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)
data = puzzle.input_data.splitlines()

total = 0
counter = [1 for _ in data]

for i, line in enumerate(data):
    cards = line.partition(':')[2].strip()
    win, _, have = cards.partition('|')
    win = {x.strip() for x in win}
    matches = sum(x.strip() in win for x in have.split())
    if matches:
        total += 2 ** (matches - 1)
    for j in range(i + 1, i + 1 + matches):
        counter[j] += counter[i]

puzzle.answer_a = total
puzzle.answer_b = sum(counter[:len(data)])
