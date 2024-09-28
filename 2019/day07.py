import asyncio
from itertools import pairwise, permutations

from more_itertools import value_chain
from aocd.models import Puzzle

from day05 import run

puzzle = Puzzle(year=2019, day=7)
data = [int(x) for x in puzzle.input_data.split(',')]


async def main_a():
    m = 0
    for p in permutations(range(5), 5):
        queues = [asyncio.Queue() for _ in range(6)]
        for q, x in zip(queues, p):
            q.put_nowait(x)
        queues[0].put_nowait(0)
        async with asyncio.TaskGroup() as group:
            for pair in pairwise(queues):
                group.create_task(run(data, *pair))
        m = max(m, queues[-1].get_nowait())
    return m


puzzle.answer_a = asyncio.run(main_a())


async def main_b():
    m = 0
    for p in permutations(range(5, 10), 5):
        queues = [asyncio.Queue() for _ in range(5)]
        for q, x in zip(queues, p):
            q.put_nowait(x)
        queues[0].put_nowait(0)
        async with asyncio.TaskGroup() as group:
            for pair in pairwise(value_chain(queues, queues[0])):
                group.create_task(run(data, *pair))
        m = max(m, queues[0].get_nowait())
    return m

puzzle.answer_b = asyncio.run(main_b())
