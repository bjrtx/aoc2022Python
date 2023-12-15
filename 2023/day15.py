import functools
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=15)
data = puzzle.input_data.split(',')


def hash_alg(s):
    return functools.reduce(lambda x, y: ((x + ord(y)) * 17) % 256, s, 0)


puzzle.answer_a = sum(hash_alg(s) for s in data)

boxes = [[] for _ in range(256)]
for s in data:
    label, symbol, focal = re.match(r'(\w+)([-=])(\w*)', s).groups()
    index = hash_alg(label)
    match symbol:
        case '-':
            boxes[index] = [b for b in boxes[index] if b[0] != label]
        case '=':
            for b in boxes[index]:
                if b[0] == label:
                    b[1] = int(focal)
                    break
            else:
                boxes[index].append([label, int(focal)])

puzzle.answer_b = sum(
    i * sum(j * f for j, (_, f) in enumerate(b, 1))
    for i, b in enumerate(boxes, 1)
)
