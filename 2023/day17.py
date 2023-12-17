import heapq
import itertools

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
data = puzzle.input_data.splitlines()

hmap = [[int(c) for c in row] for row in data]
m, n = len(hmap), len(hmap[0])


def neighbours(i, j, vertical=True, second_part=False):
    dx, dy = (0, 1) if vertical else (1, 0)
    return filter(
        lambda p: 0 <= p[0] < m and 0 <= p[1] < n,
        (
            (i + nb * a * dx, j + nb * b * dy, not vertical)
            for a, b in itertools.product((-1, 1), repeat=2)
            for nb in (range(4, 11) if second_part else range(1, 4))
        )
    )


def distance(a, b):
    (i, j, *_), (ii, jj, *_) = a, b
    return (
        sum(hmap[i][jjj] for jjj in range(jj, j, -1 if j <= jj else 1))
        if i == ii
        else sum(hmap[iii][j] for iii in range(ii, i, -1 if i <= ii else 1))
    )


def answer(second_part=False):
    q = [(0, (0, 0, b)) for b in (True, False)]
    dist = {}
    while q:
        curr_d, curr = heapq.heappop(q)
        if curr not in dist:
            dist[curr] = curr_d
            for neighbour in set(neighbours(*curr, second_part)).difference(dist):
                heapq.heappush(q, (curr_d + distance(curr, neighbour), neighbour))
    return min(dist[(m - 1, n - 1, b)] for b in (True, False))


puzzle.answer_a, puzzle.answer_b = map(answer, (False, True))
