import json

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=12)
data = json.loads(puzzle.input_data)


def value(obj, first_step=True):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(value(o, first_step) for o in obj)
    elif isinstance(obj, dict) and (first_step or "red" not in obj.values()):
        return sum(value(o, first_step) for o in obj.values())
    else:
        return 0


puzzle.answer_a = value(data, first_step=True)
puzzle.answer_b = value(data, first_step=False)
