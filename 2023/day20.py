import copy
import itertools
import math
from collections import defaultdict, deque
from functools import cache
from operator import itemgetter

import more_itertools
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=20)
data = puzzle.input_data.splitlines()

types: defaultdict[str, str | None] = defaultdict(lambda: None)
dest = defaultdict(list)
for line in data:
    left, right = line.split(' -> ')
    if left.startswith('%'):
        types[left[1:]] = 'flip-flop'
    elif left.startswith('&'):
        types[left[1:]] = 'conj'
    dest[left.lstrip('&%')] = right.split(', ')

modules = set(dest)
inputs = defaultdict(list) | more_itertools.map_reduce(
    ((l, r) for l, v in dest.items() for r in v),
    keyfunc=itemgetter(1),
    valuefunc=itemgetter(0)
)

state = {}


def clean_state():
    for module in modules:
        if types[module] == 'flip-flop':
            state[module] = False
        elif types.get(module) == 'conj':
            state[module] = {k: False for k in inputs[module]}


tot = [0, 0]


def push():
    pulses = deque([('broadcaster', 'button', False)])
    while pulses:
        module, source, high = pulses.popleft()
        tot[high] += 1
        match types[module]:
            case 'flip-flop':
                if not high:
                    state[module] = not state[module]
                    pulses.extend((x, module, state[module]) for x in dest[module])
            case 'conj':
                state[module][source] = high
                send_high = not all(state[module].values())
                pulses.extend((x, module, send_high) for x in dest[module])
            case None:
                pulses.extend((x, module, False) for x in dest[module])
    return copy.deepcopy(state)


clean_state()
for _ in range(1000):
    push()
puzzle.answer_a = math.prod(tot)


@cache
def indirect_inputs(module):
    return more_itertools.first(
        more_itertools.duplicates_justseen(
            more_itertools.iterate(
                lambda s: s.union(*(inputs[m] for m in s)),
                set(inputs[module])
            )
        )
    )


cache_ = dict()


def period(module):
    global cache_
    if module in cache_:
        return cache_[module]
    r = indirect_inputs(module)
    clean_state()
    seen = dict()
    for i in itertools.count():
        h = push()
        h = repr([h.get(s) for s in r])
        if delta := seen.setdefault(h, i) - i:
            cache_.update((s, delta) for s in r | {module})
            return delta
        seen[h] = i


#  Visual inspection, 'tg' is the top-most module
puzzle.answer_b = math.lcm(*(period(m) for m in modules - {'tg'}))
