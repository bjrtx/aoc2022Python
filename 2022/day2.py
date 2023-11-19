from aocd.models import Puzzle

puzzle = Puzzle(2022, 2)
data = puzzle.input_data.splitlines()


def score_a(opp_char, my_char):
    opp_strat = ord(opp_char) - ord('A')
    my_strat = ord(my_char) - ord('X')
    return (1 + my_strat) + (0 if (my_strat + 1) % 3 == opp_strat else 3 if my_strat == opp_strat else 6)


def score_b(opp_char, my_char):
    opp_strat = ord(opp_char) - ord('A')
    if my_char == 'Y':
        my_strat = opp_strat
    elif my_char == 'X':
        my_strat = (opp_strat - 1) % 3
    else:
        my_strat = (opp_strat + 1) % 3
    return (1 + my_strat) + (0 if (my_strat + 1) % 3 == opp_strat else 3 if my_strat == opp_strat else 6)


puzzle.answer_a = sum(score_a(*line.split()) for line in data)
puzzle.answer_b = sum(score_b(*line.split()) for line in data)
