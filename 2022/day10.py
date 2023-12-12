from aocd.models import Puzzle

puzzle = Puzzle(2022, 10)
data = puzzle.input_data.splitlines()
instructions = [line.split() for line in data]


def values():
    time = 1
    value = 1
    for instr in instructions:
        # noinspection SpellCheckingInspection
        if instr[0] == "addx":
            time += 2
            value += int(instr[1])
            yield time, value
        else:
            time += 1


value_list = list(values())


def value_at_time(time):
    res = 1
    for t, v in value_list:
        if t <= time:
            res = v
    return res


puzzle.answer_a = sum(t * value_at_time(t) for t in range(20, 221, 40))


def displayed():
    stack = list(reversed(value_list))
    pos = 0
    time = 0
    for line in range(6):
        for char in range(40):
            time += 1
            if stack and time == stack[-1][0]:
                _, pos = stack.pop()
            if abs(pos - char) <= 1:
                yield "#"
            else:
                yield "."
        yield "\n"


# noinspection SpellCheckingInspection
puzzle.answer_b = "ERCREPCJ"
