import math
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2015, day=16)
data = puzzle.input_data.splitlines()

info = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

info_dict = {m[1]: int(m[2]) for m in re.finditer(r'(\w+): (\d+)', info)}


def is_compatible(aunt: dict):
    return all(
        info_dict.get(k, None) == v
        for k, v in aunt.items()
    )


def is_compatible2(aunt: dict):
    return all((
        all(
            info_dict.get(k, None) == v
            for k, v in aunt.items()
            if k not in ["cats", "trees", "pomeranians", "goldfish"]
        ),
        aunt.get("cats", math.inf) > info_dict["cats"],
        aunt.get("trees", math.inf) > info_dict["trees"],
        aunt.get("pomenaranians", -math.inf) < info_dict["pomeranians"],
        aunt.get("goldfish", -math.inf) < info_dict["goldfish"]
    ))


data = (line.partition(':')[-1] for line in data)
aunts = [{m[1]: int(m[2]) for m in re.finditer(r'(\w+): (\d+)', line)} for line in data]

puzzle.answer_a = next(i for i, aunt in enumerate(aunts, 1) if is_compatible(aunt))
puzzle.answer_b = next(i for i, aunt in enumerate(aunts, 1) if is_compatible2(aunt))
