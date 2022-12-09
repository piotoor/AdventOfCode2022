import math

from utilities import non_blank_lines


def parse_day9_a():
    with open("day9.txt", "r") as f:
        data = [(line.split()[0], int(line.split()[1])) for line in non_blank_lines(f)]

    return data


NO_OF_KNOTS = 10
H = 0
T = NO_OF_KNOTS - 1
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

    if dx == -2:
        t[X] -= 1
        t[Y] += math.copysign(1, dy) if dy != 0 else 0
    elif dx == 2:
        t[X] += 1
        t[Y] += math.copysign(1, dy) if dy != 0 else 0
    elif dy == -2:
        t[Y] -= 1
        t[X] += math.copysign(1, dx) if dx != 0 else 0
    elif dy == 2:
        t[Y] += 1
        t[X] += math.copysign(1, dx) if dx != 0 else 0

    return t


def count_places_visited_by_tail(data):
    visited = set()

    h_pos = [0, 0]
    t_pos = [0, 0]

    for d, n in data:
        for i in range(n):
            h_pos = move_head(h_pos, d)
            t_pos = move_tail(h_pos, t_pos)

            visited.add(tuple(t_pos))

    return len(visited)


def day9_a():
    data = parse_day9_a()
    print("day9_a = {}".format(count_places_visited_by_tail(data)))


def print_knots(data):
    board = [["." for _ in range(40)] for _ in range(40)]
    for i in range(len(data)):
        if i == 0:
            c = 'H'
        elif i == 9:
            c = 'T'
        else:
            c = str(i)
        board[data[i][1] + 20][data[i][0] + 20] = c

    for x in board:
        print(x)


def count_places_visited_by_tail_10(data):
    visited = {(0, 0)}
    knots = [[0, 0] for _ in range(NO_OF_KNOTS)]

    for d, n in data:
        for i in range(n):
            knots[H] = move_head(knots[H], d)
            for j in range(1, NO_OF_KNOTS):
                knots[j] = move_tail(knots[j - 1], knots[j])

            visited.add(tuple(knots[T]))

    return len(visited)


def day9_b():
    data = parse_day9_a()
    print("day9_b = {}".format(count_places_visited_by_tail_10(data)))
