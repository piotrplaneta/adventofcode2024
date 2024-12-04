input: list[str] = []
with open("input/day04") as f:
    for l in f:
        input.append(l.strip())

possible_mas_positions = [
    [[1, 0], [2, 0], [3, 0]],
    [[1, 1], [2, 2], [3, 3]],
    [[0, 1], [0, 2], [0, 3]],
    [[-1, 1], [-2, 2], [-3, 3]],
    [[-1, 0], [-2, 0], [-3, 0]],
    [[-1, -1], [-2, -2], [-3, -3]],
    [[0, -1], [0, -2], [0, -3]],
    [[1, -1], [2, -2], [3, -3]],
]


def is_coord_valid(x, y):
    if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input):
        return False

    return True


def are_possible_mas_postions_valid(
    start_x: int, start_y: int, deltas: list[list[int]]
):
    for i in range(3):
        if not is_coord_valid(start_x + deltas[i][0], start_y + deltas[i][1]):
            return False

    return True


def is_mas(start_x: int, start_y: int, deltas: list[list[int]]):
    if not are_possible_mas_postions_valid(start_x, start_y, deltas):
        return False

    letters = ["M", "A", "S"]

    for i in range(3):
        if not input[start_y + deltas[i][1]][start_x + deltas[i][0]] == letters[i]:
            return False

    return True


def xmas_count_starting_at(x, y):
    count = 0
    for mas_position in possible_mas_positions:
        if is_mas(x, y, mas_position):
            count += 1

    return count


xmas_count = 0
for y in range(len(input)):
    line = input[y]

    for x in range(len(line)):
        if line[x] == "X":
            xmas_count += xmas_count_starting_at(x, y)

print(xmas_count)

x_mas_count = 0


def is_x_mas_possible(x, y):
    possible_deltas = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

    for d in possible_deltas:
        if not is_coord_valid(x + d[0], y + d[1]):
            return False

    return True


def at(x, y, dx, dy):
    return input[y + dy][x + dx]


def has_x_mas_at(x, y):
    if not is_x_mas_possible(x, y):
        return False

    left_to_right = (at(x, y, -1, -1) == "M" and at(x, y, 1, 1) == "S") or (
        at(x, y, -1, -1) == "S" and at(x, y, 1, 1) == "M"
    )

    right_to_left = (at(x, y, 1, -1) == "M" and at(x, y, -1, 1) == "S") or (
        at(x, y, 1, -1) == "S" and at(x, y, -1, 1) == "M"
    )

    return left_to_right and right_to_left


for y in range(len(input)):
    line = input[y]

    for x in range(len(line)):
        if line[x] == "A" and has_x_mas_at(x, y):
            x_mas_count += 1


print(x_mas_count)
