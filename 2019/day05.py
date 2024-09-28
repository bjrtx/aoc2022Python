import asyncio
from collections import defaultdict

from aocd.models import Puzzle
from more_itertools import iter_suppress, one, repeatfunc

puzzle = Puzzle(year=2019, day=5)
data = [int(x) for x in puzzle.input_data.split(',')]


async def run(data, input_: asyncio.Queue, output: asyncio.Queue):
    pointer = 0
    rel_base = 0
    memory = defaultdict(int, enumerate(data))

    while pointer < len(memory):
        modes = [(memory[pointer] // d) % 10 for d in (100, 1_000, 10_000)]

        def read(idx, pos):
            match modes[pos - 1]:
                case 0:
                    return memory[memory[idx + pos]]
                case 1:
                    return memory[idx + pos]
                case 2:
                    return memory[memory[idx + pos] + rel_base]
                case _:
                    raise RuntimeError

        def write(idx, pos, val):
            match modes[pos - 1]:
                case 0:
                    location = memory[idx + pos]
                case 2:
                    location = memory[idx + pos] + rel_base
                case _:
                    raise RuntimeError
            memory[location] = val

        match memory[pointer] % 100:
            case 1:
                write(pointer, 3, read(pointer, 1) + read(pointer, 2))
                pointer += 4
            case 2:
                write(pointer, 3, read(pointer, 1) * read(pointer, 2))
                pointer += 4
            case 3:
                write(pointer, 1, await input_.get())
                pointer += 2
            case 4:
                await output.put(read(pointer, 1))
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
                write(pointer, 3, int(read(pointer, 1) < read(pointer, 2)))
                pointer += 4
            case 8:
                write(pointer, 3, int(read(pointer, 1) == read(pointer, 2)))
                pointer += 4
            case 9:
                rel_base += int(read(pointer, 1))
                pointer += 2
            case 99:
                return


if __name__ == '__main__':
    i, o = asyncio.Queue(), asyncio.Queue()
    i.put_nowait(1)
    asyncio.run(run(data, input_=i, output=o))
    puzzle.answer_a = one(
        filter(
            None,
            iter_suppress(repeatfunc(o.get_nowait), asyncio.QueueEmpty))
    )
    i.put_nowait(5)
    asyncio.run(run(data, input_=i, output=o))
    puzzle.answer_b = one(
        filter(
            None,
            iter_suppress(repeatfunc(o.get_nowait), asyncio.QueueEmpty))
    )
