from collections import Counter

input = []
with open("input/day01") as f:
    for l in f:
        input.append(l.strip().split("   "))

l1 = [int(i[0]) for i in input]
l2 = [int(i[1]) for i in input]

in_order = zip(sorted(l1), sorted(l2))
print(sum([abs(p[0] - p[1]) for p in in_order]))

counts = Counter(l2)
print(sum([n * counts.get(n, 0) for n in l1]))
