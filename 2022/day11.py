import heapq
import itertools
import re
from collections import deque, Counter
from math import lcm

from aocd.models import Puzzle

puzzle = Puzzle(2022, 11)
data = puzzle.input_data


class Monkey():
    def __init__(self, items: deque[int], expr, test, if_true, if_false):
        self.items = items
        self.expr = expr
        self.test = test
        self.if_true = if_true
        self.if_false = if_false


pattern = r"""Monkey (\d+):
  Starting items: (?P<items>(?:\d+, )*\d+)
  Operation: new = (?P<expr>.*)
  Test: divisible by (?P<div>\d+)
    If true: throw to monkey (?P<true>\d+)
    If false: throw to monkey (?P<false>\d+)"""
monkeys = [
    Monkey(
        items=deque(list(eval(m["items"] + ","))),
        expr = m["expr"],
        test=int(m["div"]),
        if_true=int(m["true"]),
        if_false=int(m["false"])
    )
    for m in re.finditer(pattern, data)
]

inspections = [0 for _ in monkeys]
mod = lcm(*(m.test for m in monkeys))

def round(relax=True, log=True):
    for i, m in enumerate(monkeys):
        if log: print(f"Monkey {i}:")
        while m.items:
            inspections[i] += 1
            item = m.items.popleft()
            if log:
                print(f"  Monkey inspects an item with a worry level of {item}.")
            new_worry = eval(m.expr.replace("old", str(item))) % mod
            if log:
                print(f"  New worry {new_worry}.")
            if relax:
                new_worry //= 3
                if log:
                    print(f"  Monkey gets bored with item. Worry level is divided by 3 to {new_worry}.")
            test = not(new_worry % m.test)
            if log:
                print(f"  Current worry level is{'' if test else ' not'} divisible by {m.test}.")
            next_monkey = m.if_true if test else m.if_false
            monkeys[next_monkey].items.append(new_worry)
            if log:
                print(f"  Item with worry level {new_worry} is thrown to monkey {next_monkey}.")

for _ in range(20): round()

a, b = heapq.nlargest(2, inspections)
puzzle.answer_a = a * b

monkeys = [
    Monkey(
        items=deque(list(eval(m["items"] + ","))),
        expr = m["expr"],
        test=int(m["div"]),
        if_true=int(m["true"]),
        if_false=int(m["false"])
    )
    for m in re.finditer(pattern, data)
]

inspections = [0 for _ in monkeys]

for _ in range(10_000): round(relax=False, log=False)
a, b = heapq.nlargest(2, inspections)
puzzle.answer_b = a * b