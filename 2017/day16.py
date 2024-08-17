from aocd.models import Puzzle
from sympy.combinatorics import Permutation

puzzle = Puzzle(year=2017, day=16)
data = puzzle.input_data.split(',')


def dance(size=16, iterations=1):
    p = Permutation(size - 1)
    q = Permutation(size - 1)
    for move in data:
        match move[0]:
            case 's':
                X = int(move[1:])
                p = Permutation(list(range(size - X, size)) + list(range(size - X))) * p
            case 'x':
                a, b = [int(x) for x in move[1:].split('/')]
                p = Permutation(a, b) * p
            case 'p':
                a, b = move[1:].split('/')
                q *= Permutation(ord(a) - ord('a'), ord(b) - ord('a'))
    return ''.join(chr(ord('a') + i) for i in (p ** iterations) * (q ** iterations))


puzzle.answer_a = dance()
puzzle.answer_b = dance(iterations=1_000_000_000)
