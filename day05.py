from functools import cmp_to_key
from filecmp import cmp
from collections import defaultdict

input: list[str] = []
with open("input/day05") as f:
    input = [l.strip() for l in f.readlines()]


rules = defaultdict(lambda: [])
tests = []

for l in input:
    splitted = l.split("|")
    if len(l.split("|")) == 2:
        rules[int(splitted[0])].append(int(splitted[1]))

    elif l != "":
        tests.append([int(n) for n in l.split(",")])


def has_incoming_edges(v: int, subset_rules):
    for k, vs_with_incoming in subset_rules.items():
        if v in vs_with_incoming:
            return True

    return False


def sort_subset(subset_vs: list[int]):
    subset_rules = defaultdict(lambda: [])

    for source_v, dest_vs in rules.items():
        if source_v in subset_vs:
            subset_rules[source_v] = [
                dest_v for dest_v in dest_vs if dest_v in subset_vs
            ]

    start_vs = set(subset_vs)
    for k, vs_with_incoming in subset_rules.items():
        for v in vs_with_incoming:
            if v in start_vs:
                start_vs.remove(v)

    in_topological_order = []

    while not len(start_vs) == 0:
        start_v = start_vs.pop()

        in_topological_order.append(start_v)
        for v in subset_rules[start_v]:
            subset_rules[start_v] = [w for w in subset_rules[start_v] if w != v]
            if not has_incoming_edges(v, subset_rules):
                start_vs.add(v)

    return in_topological_order


sum_part1 = 0
sum_part2 = 0

for test in tests:
    in_topological_order = sort_subset(test)

    def topological_cmp(x, y):
        return in_topological_order.index(x) - in_topological_order.index(y)

    in_order = sorted(test, key=cmp_to_key(topological_cmp))

    if in_order == test:
        sum_part1 += test[len(test) // 2]
    else:
        sum_part2 += in_order[len(in_order) // 2]


print(sum_part1)
print(sum_part2)
