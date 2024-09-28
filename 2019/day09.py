import asyncio

from aocd.models import Puzzle

from day05 import run

puzzle = Puzzle(year=2019, day=9)
data = [int(x) for x in puzzle.input_data.split(',')]


i, o = asyncio.Queue(), asyncio.Queue()
i.put_nowait(1)
asyncio.run(run(data, input_=i, output=o))
puzzle.answer_a = o.get_nowait()
i.put_nowait(2)
asyncio.run(run(data, input_=i, output=o))
puzzle.answer_b = o.get_nowait()
