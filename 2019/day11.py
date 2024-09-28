import asyncio
from collections import defaultdict

import numpy as np
from aocd.models import Puzzle

from day05 import run

puzzle = Puzzle(year=2019, day=11)
data = [int(x) for x in puzzle.input_data.split(',')]


class Robot:
    def __init__(self, color=0):
        self.panels = defaultdict(int) | {(0, 0): color}
        self.pos = np.zeros(2, dtype=int)
        self.dir = np.array([0, -1], dtype=int)
        self.input_, self.output = asyncio.Queue(), asyncio.Queue()
        self.brain = run(data, self.input_, self.output)
        self.painted = set()

    async def pilot(self):
        while True:
            curr_color = int(self.panels[tuple(self.pos)])
            await self.input_.put(curr_color)
            color = await self.output.get()
            if color != curr_color:
                self.panels[tuple(self.pos)] = color
                self.painted.add(tuple(self.pos))
            if await self.output.get():
                self.dir = np.array([self.dir[1], -self.dir[0]])
            else:
                self.dir = np.array([-self.dir[1], self.dir[0]])
            self.pos += self.dir

    async def run(self):
        async with asyncio.TaskGroup() as group:
            b = group.create_task(self.brain)
            p = group.create_task(self.pilot())
            b.add_done_callback(p.cancel)


r = Robot(color=0)
asyncio.run(r.run())
puzzle.answer_a = len(r.painted)

r = Robot(color=1)
asyncio.run(r.run())
x_m = min(x for x, _ in r.panels)
x_M = max(x for x, _ in r.panels)
y_m = min(y for _, y in r.panels)
y_M = max(y for _, y in r.panels)
for j in range(y_m, y_M + 1):
    for i in range(x_M, x_m, -1):
        print('▮' if r.panels[i, j] else '▯', end='')
    print()
