import copy

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=5)
data = [int(x) for x in puzzle.input_data.split(',')]


def run(input_):
    pointer = 0
    memory = copy.deepcopy(data)

    while pointer < len(memory):
        modes = [(memory[pointer] // d) % 10 for d in (100, 1_000, 10_000)]

        def read(idx, pos):
            return memory[idx + pos] if modes[pos - 1] else memory[memory[idx + pos]]

        match memory[pointer] % 100:
            case 1:
                memory[memory[pointer + 3]] = read(pointer, 1) + read(pointer, 2)
                pointer += 4
            case 2:
                memory[memory[pointer + 3]] = read(pointer, 1) * read(pointer, 2)
                pointer += 4
            case 3:
                memory[memory[pointer + 1]] = input_
                pointer += 2
            case 4:
                input_ = read(pointer, 1)
                pointer += 2
            case 5:
                if read(pointer, 1):
                    pointer = read(pointer, 2)
                else:
                    pointer += 3
            case 6:
                if not read(pointer, 1):
                    pointer = read(pointer, 2)
                else:
                    pointer += 3
            case 7:
                memory[memory[pointer + 3]] = int(read(pointer, 1) < read(pointer, 2))
                pointer += 4
            case 8:
                memory[memory[pointer + 3]] = int(read(pointer, 1) == read(pointer, 2))
                pointer += 4
            case 99:
                break
    return input_


puzzle.answer_a = run(1)
puzzle.answer_b = run(5)
