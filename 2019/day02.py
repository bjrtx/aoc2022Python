import copy
import itertools

import more_itertools
from aocd.models import Puzzle
from more_itertools import first

puzzle = Puzzle(year=2019, day=2)
data = [int(x) for x in puzzle.input_data.split(',')]



def run(noun, verb):
    pointer = 0
    memory = copy.deepcopy(data)
    memory[1] = noun
    memory[2] = verb
    while pointer < len(memory):
        match memory[pointer]:
            case 1:
                memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
            case 2:
                memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
            case 99:
                break
        pointer += 4
    return memory[0]

puzzle.answer_a = run(12, 2)
puzzle.answer_b = first(
    100 * noun + verb
    for noun, verb in itertools.product(range(100), repeat=2)
    if run(noun, verb) == 19690720
)