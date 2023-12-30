from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=8)
data = puzzle.input_data.splitlines()


def run():
    accumulator = 0
    pos = 0
    seen = set()

    while True:
        if pos in seen:
            return accumulator, False
        elif pos not in range(len(data)):
            return accumulator, pos == len(data)
        else:
            seen.add(pos)
            instruction, value = data[pos].split()
            match instruction:
                case 'acc':
                    accumulator += int(value)
                    pos += 1
                case 'jmp':
                    pos += int(value)
                case 'nop':
                    pos += 1


puzzle.answer_a, _ = run()

for i, line in enumerate(data):
    data[i] = line.replace('nop', 'jmp') if line.startswith('nop') else line.replace('jmp', 'nop')
    acc, test = run()
    if test:
        break
    data[i] = line.replace('jmp', 'nop') if line.startswith('nop') else line.replace('nop', 'jmp')

puzzle.answer_b = acc
