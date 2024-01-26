from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=3)
data = [line.split(',') for line in puzzle.input_data.splitlines()]


def follow(wire):
    x, y = 0, 0
    time = 0
    for entry in wire:
        match [entry[0], int(entry[1:])]:
            case ['R', n]:
                for _ in range(n):
                    y += 1
                    time += 1
                    yield time, x, y
            case ['L', n]:
                for _ in range(n):
                    y -= 1
                    time += 1
                    yield time, x, y
            case ['U', n]:
                for _ in range(n):
                    x += 1
                    time += 1
                    yield time, x, y
            case ['D', n]:
                for _ in range(n):
                    x -= 1
                    time += 1
                    yield time, x, y


visit1, visit2 = dict(), dict()
for t, x, y in follow(data[0]):
    visit1.setdefault((x, y), t)
for t, x, y in follow(data[1]):
    visit2.setdefault((x, y), t)
intersections = set(visit1).intersection(visit2)
puzzle.answer_a = min(abs(x) + abs(y) for x, y in intersections)
puzzle.answer_b = min(visit1[pos] + visit2[pos] for pos in intersections)
