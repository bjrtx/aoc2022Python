from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=4)
data = puzzle.input_data.splitlines()


def is_valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


puzzle.answer_a = sum(is_valid(passphrase) for passphrase in data)


def is_still_valid(passphrase):
    words = [tuple(sorted(w)) for w in passphrase.split()]
    return len(words) == len(set(words))


puzzle.answer_b = sum(is_still_valid(passphrase) for passphrase in data)
