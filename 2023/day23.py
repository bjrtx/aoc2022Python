import itertools
from collections import defaultdict
from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=23)
data = puzzle.input_data.splitlines()

m, n = len(data), len(data[0])
start = 0, data[0].index('.')
end = m - 1, data[-1].index('.')


@cache
def neighbours(pos):
    i, j = pos
    match data[i][j]:
        case '^':
            adj = ((i - 1, j),)
        case 'v':
            adj = ((i + 1, j),)
        case '<':
            adj = ((i, j - 1),)
        case '>':
            adj = ((i, j + 1),)
        case _:
            adj = four_neighbourhood(pos)
    return {
        (x, y)
        for x, y in adj
        if x in range(m) and y in range(n) and data[x][y] != '#'
    }


def four_neighbourhood(pos):
    i, j = pos
    return (
        (x, y)
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        if x in range(m) and y in range(n) and data[x][y] != '#'
    )


forks = {
    (i, j) for i in range(m) for j in range(n)
    if data[i][j] != '#' and len(neighbours((i, j))) > 2
} | {start, end}


@cache
def fork_neighbours(pos: tuple[int, int]) -> dict[tuple[int, int], int]:
    stack = [(neighbour, 1) for neighbour in four_neighbourhood(pos)]
    seen = {pos}
    r = defaultdict(int)
    while stack:
        curr, dist = stack.pop()
        if curr in forks and curr != pos:
            r[curr] = max(r[curr], dist)
        elif curr not in seen:
            seen.add(curr)
            stack.extend((nb, dist + 1) for nb in four_neighbourhood(curr))
    return r


def all_paths(start, end, neighbours):
    seen, path = {start}, [start]
    stack = [(x, start) for x in neighbours(start)]
    while stack:
        curr, parent = stack.pop()
        while path and parent != path[-1]:
            seen.remove(path.pop())
        assert len(seen) == len(path)

        if curr == end:
            yield *path, end
        else:
            path.append(curr)
            seen.add(curr)
            neighb = neighbours(curr) - seen
            stack.extend([(x, curr) for x in neighb])


puzzle.answer_a = max(len(p) - 1 for p in all_paths(start, end, neighbours=neighbours))


# ca. 40 seconds
puzzle.answer_b = max(
    sum(fork_neighbours(a)[b] for a, b in itertools.pairwise(p))
    for p in all_paths(start, end, neighbours=lambda x: set(fork_neighbours(x)))
)
