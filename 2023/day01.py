from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)
data = puzzle.input_data.splitlines()


def integers(s: str, first_step=True):
    for j, c in enumerate(s):
        if c.isnumeric():
            yield int(c)
        elif not first_step:
            for i, w in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], start=1):
                if s.startswith(w, j):
                    yield i
                    break


def solve(first_step=True):
    ints = (list(integers(line, first_step)) for line in data)
    return sum(c[0] * 10 + c[-1] for c in ints)


puzzle.answer_a = solve(first_step=True)
puzzle.answer_b = solve(first_step=False)
