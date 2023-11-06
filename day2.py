from aocd.models import Puzzle


puzzle = Puzzle(2022, 2)


def score(opp_char, my_char):
    opp_strat = ord(opp_char) - ord('A')
    my_strat = ord(my_char) - ord('X')
    return (1 + my_strat) + (0 if (my_strat + 1) % 3 == opp_strat else 3 if my_strat == opp_strat else 6)

puzzle.answer_a = sum(score(*line.split()) for line in puzzle.input_data.splitlines())
