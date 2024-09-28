import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=8)
data = puzzle.input_data

WIDTH, HEIGHT = 25, 6
layers = list(itertools.batched(data, WIDTH * HEIGHT))

layer = min(layers, key=lambda t: t.count('0'))
puzzle.answer_a = layer.count('1') * layer.count('2')

values = [
    next((x for x in ls if x != '2'), '2')
    for ls in zip(*layers)
]
message = '\n'.join(
    ''.join('▯' if c == '0' else '▮' for c in v)
    for v in itertools.batched(values, WIDTH))
print(message)
