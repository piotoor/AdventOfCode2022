import math

from utilities import non_blank_lines


def parse_day9_a():
    with open("day9.txt", "r") as f:
        data = [(line.split()[0], int(line.split()[1])) for line in non_blank_lines(f)]

    return data


NO_OF_KNOTS_A = 2
NO_OF_KNOTS_B = 10
H = 0
X = 0
Y = 1


def move_head(h, d):
    if d == "R":
        h[X] += 1
    elif d == "L":
        h[X] -= 1
    elif d == "U":
        h[Y] += 1
    elif d == "D":
        h[Y] -= 1

    return h


def move_tail(h, t):
    dx = h[X] - t[X]
    dy = h[Y] - t[Y]

    if abs(dx) == 2:
        t[X] += math.copysign(1, dx)
        t[Y] += math.copysign(1, dy) if dy != 0 else 0
    elif abs(dy) == 2:
        t[Y] += math.copysign(1, dy)
        t[X] += math.copysign(1, dx) if dx != 0 else 0

    return t


def count_places_visited_by_tail(data, num_of_knots):
    visited = {(0, 0)}
    knots = [[0, 0] for _ in range(num_of_knots)]

    for d, n in data:
        for i in range(n):
            knots[H] = move_head(knots[H], d)
            for j in range(1, num_of_knots):
                knots[j] = move_tail(knots[j - 1], knots[j])

            visited.add(tuple(knots[-1]))

    return len(visited)


def day9_a():
    data = parse_day9_a()
    print("day9_a = {}".format(count_places_visited_by_tail(data, NO_OF_KNOTS_A)))


# def print_knots(data):
#     board = [["." for _ in range(40)] for _ in range(40)]
#     for i in range(len(data)):
#         if i == 0:
#             c = 'H'
#         elif i == 9:
#             c = 'T'
#         else:
#             c = str(i)
#         board[data[i][1] + 20][data[i][0] + 20] = c
#
#     for x in board:
#         print(x)


def day9_b():
    data = parse_day9_a()
    print("day9_b = {}".format(count_places_visited_by_tail(data, NO_OF_KNOTS_B)))
