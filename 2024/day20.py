import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=20)
data = puzzle.input_data

track = np.array([list(row) for row in data.splitlines()])
track_dist = np.where(track != '#', 0, -1)
m, n = track.shape
((i, j),) = np.argwhere(track == 'S')
track_dist[i, j] = idx = 1
while True:
    neighb = [
        (x, y)
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
        if track_dist[x, y] == 0]
    if not neighb:
        break
    else:
        i, j = more_itertools.one(neighb)
        idx += 1
        track_dist[i, j] = idx


def cheats(r):
    for i, j in np.argwhere(track_dist != - 1):
        reachable = (
            (i + di, j + dj, abs(di) + abs(dj))
            for di in range(-r, r + 1)
            if 0 <= i + di < m
            for dj in range(-r + abs(di), r + 1 - abs(di))
            if 0 <= j + dj < n and (di, dj) != (0, 0)
        )
        yield from (
            track_dist[x, y] - track_dist[i, j] - d >= 100
            for x, y, d in reachable
        )


puzzle.answer_a, puzzle.answer_b = (str(sum(cheats(r))) for r in (2, 20))
