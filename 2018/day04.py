import itertools
import re
from collections import Counter, defaultdict
from operator import itemgetter

import more_itertools
import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2018, day=4)
data = puzzle.input_data.splitlines()

events = [
    re.fullmatch(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})] (.*)', line).groups()
    for line in data
]
events.sort()
ranges = defaultdict(list)
shifts = more_itertools.split_before(events, lambda t:t[-1].endswith('shift'))
for s in shifts:
    guard_id = int(re.search(r'#(\d+)', s[0][-1])[1])
    for a, b in itertools.batched(s[1:], 2):
        ranges[guard_id].append(range(int(a[-2]), int(b[-2])))

guard, naps = max(ranges.items(), key=lambda t: sum(len(r) for r in t[1]))
(minute, _), *_ = Counter(itertools.chain(*naps)).most_common(1)
puzzle.answer_a = guard * minute

guard, minute, _ = max(
    (
        (guard, *(Counter(itertools.chain(*naps)).most_common(1)[0]))
        for guard, naps in ranges.items()
    ),
    key=itemgetter(2)
)
puzzle.answer_b = guard * minute
