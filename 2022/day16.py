import re
from functools import cache

import networkx
from aocd.models import Puzzle

puzzle = Puzzle(2022, 16)
data = puzzle.examples[0].input_data.splitlines()
data = puzzle.input_data.splitlines()

connections = dict()
flows = dict()
g = networkx.Graph()
for line in data:
    m = re.match(
        r'Valve ([A-Z]{2}) has flow rate=(\d+);'
        r' (?:tunnels lead to valves ((?:[A-Z]{2}, )*[A-Z]{2})'
        r'|tunnel leads to valve ([A-Z]{2}))',
        line
    )
    valve, flow, leads = [p for p in m.groups() if p]
    flows[valve] = int(flow)
    g.add_edges_from((valve, n) for n in leads.split(', '))

length: dict[str, dict[str, int]] = dict(networkx.all_pairs_shortest_path_length(g))
relevant = {n for n, v in flows.items() if v}


@cache
def optimal(remains: frozenset[str] = frozenset(relevant), position: str = 'AA', time: int = 30):
    def possible():
        for n in remains:
            d: int = length[n][position]
            if d < time:
                yield optimal(remains - {n}, n, time - d - 1) + (time - d - 1) * flows[n]

    return max(possible(), default=0)


puzzle.answer_a = optimal()
