input = []
with open("input/day02") as f:
    for l in f:
        input.append(l.strip().split(" "))

input = [[int(i) for i in l] for l in input]


def is_safe(line: list[int]):
    init_delta = line[1] - line[0]

    if abs(init_delta) < 1 or abs(init_delta) > 3:
        return False

    for i in range(2, len(line)):
        delta = line[i] - line[i - 1]

        if delta * init_delta < 0:
            return False

        if abs(delta) < 1 or abs(delta) > 3:
            return False

    return True


print(sum([is_safe(l) for l in input]))

safe = 0
for line in input:
    possible_lines = []

    for i in range(len(line)):
        possible_lines.append(line[0:i] + line[i + 1 :])

    if any(is_safe(l) for l in possible_lines):
        safe += 1

print(safe)
