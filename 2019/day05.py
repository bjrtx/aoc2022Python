import asyncio
import copy

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=5)
data = [int(x) for x in puzzle.input_data.split(',')]


async def run(data, input: asyncio.Queue, output: asyncio.Queue):
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
                memory[memory[pointer + 1]] = await input.get()
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
                memory[memory[pointer + 3]] = int(read(pointer, 1) < read(pointer, 2))
                pointer += 4
            case 8:
                memory[memory[pointer + 3]] = int(read(pointer, 1) == read(pointer, 2))
                pointer += 4
            case 99:
                return


q, o = asyncio.Queue(), asyncio.Queue()
q.put_nowait(1)
asyncio.run(run(data, input=q, output=o))
while not o.empty():
    x = o.get_nowait()
puzzle.answer_a = x
q, o = asyncio.Queue(), asyncio.Queue()
q.put_nowait(5)
asyncio.run(run(data, input=q, output=o))
while not o.empty():
    x = o.get_nowait()
puzzle.answer_b = x