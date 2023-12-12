from aocd.models import Puzzle

puzzle = Puzzle(2022, 2)
data = puzzle.input_data.splitlines()


def score_a(opp_char, my_char):
    opp_strategy = ord(opp_char) - ord('A')
    my_strategy = ord(my_char) - ord('X')
    return (1 + my_strategy) + (0 if (my_strategy + 1) % 3 == opp_strategy else 3 if my_strategy == opp_strategy else 6)


def score_b(opp_char, my_char):
    opp_strategy = ord(opp_char) - ord('A')
    if my_char == 'Y':
        my_strategy = opp_strategy
    elif my_char == 'X':
        my_strategy = (opp_strategy - 1) % 3
    else:
        my_strategy = (opp_strategy + 1) % 3
    return (1 + my_strategy) + (0 if (my_strategy + 1) % 3 == opp_strategy else 3 if my_strategy == opp_strategy else 6)


puzzle.answer_a = sum(score_a(*line.split()) for line in data)
puzzle.answer_b = sum(score_b(*line.split()) for line in data)
