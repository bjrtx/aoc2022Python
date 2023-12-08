from collections import Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=7)
data = puzzle.input_data.splitlines()

translation = {str(i): i for i in range(2, 10)} | {suit: i for i, suit in enumerate('TJQKA', 10)}

hands = [
    (h, int(bid))
    for h, bid in (line.split() for line in data)
]


def strength(hand_and_bid):
    hand, bid = hand_and_bid
    return sorted(Counter(hand).values(), reverse=True), [translation[c] for c in hand]


def joker_strength(hand_and_bid):
    hand, bid = hand_and_bid
    c = Counter(hand)
    jokers, c['J'] = c['J'], 0
    type_ = sorted(c.values(), reverse=True) or [0]
    type_[0] += jokers
    return type_, [translation[c] if c != 'J' else 0 for c in hand]


def winnings():
    return sum(i * bid for i, (_, bid) in enumerate(hands, start=1))


hands.sort(key=strength)
puzzle.answer_a = winnings()
hands.sort(key=joker_strength)
puzzle.answer_b = winnings()
