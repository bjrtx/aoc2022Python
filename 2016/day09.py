from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=9)
data = puzzle.input_data


def expanded_size(string, recursive=True):
    res = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            j = string.index(')', i)
            length, times = [int(x) for x in string[i + 1:j].split('x')]
            res += times * (
                       expanded_size(string[j + 1:j + 1 + length], recursive)
                       if recursive
                       else length)
            i = j + 1 + length
        else:
            i += 1
            res += 1
    return res


puzzle.answer_a = expanded_size(data, recursive=False)
puzzle.answer_b = expanded_size(data, recursive=True)
