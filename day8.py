from functools import reduce
from operator import mul


def parse_day8_a():
    with open("day8.txt", "r") as f:
        data = tuple(f.read().splitlines())

    return [list(map(int, x)) for x in data]


def count_visible_trees(data):
    visible = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
                visible[i][j] = 1

    ans = len(data[0]) * 2 + 2 * (len(data) - 2)

    # right
    for i in range(1, len(data) - 1):
        curr_max = data[i][0]
        for j in range(1, len(data[i]) - 1):
            if data[i][j] > curr_max:
                curr_max = data[i][j]
                if visible[i][j] == 0:
                    ans += 1
                    visible[i][j] = 1

    # left
    for i in range(1, len(data) - 1):
        curr_max = data[i][-1]
        for j in range(len(data[i]) - 2, 0, -1):
            if data[i][j] > curr_max:
                curr_max = data[i][j]
                if visible[i][j] == 0:
                    ans += 1
                    visible[i][j] = 1

    # down
    for j in range(1, len(data[0]) - 1):
        curr_max = data[0][j]
        for i in range(1, len(data) - 1):
            if data[i][j] > curr_max:
                curr_max = data[i][j]
                if visible[i][j] == 0:
                    ans += 1
                    visible[i][j] = 1

    # up
    for j in range(1, len(data[0]) - 1):
        curr_max = data[-1][j]
        for i in range(len(data) - 2, 0, -1):
            if data[i][j] > curr_max:
                curr_max = data[i][j]
                if visible[i][j] == 0:
                    ans += 1
                    visible[i][j] = 1

    return ans


def day8_a():
    data = parse_day8_a()
    print("day8_a = {}".format(count_visible_trees(data)))


def find_highest_scenic_score(data):
    # u, d, l, r - opposite to the walking direction used below
    scenic = [[[0, 0, 0, 0] for _ in range(len(data[0]))] for _ in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[0])):
            # walk left; right scenic
            for k in range(j - 1, -1, -1):
                scenic[i][j][3] += 1
                if data[i][k] >= data[i][j]:
                    break

            # walk right; left scenic
            for k in range(j + 1, len(data[i])):
                scenic[i][j][2] += 1
                if data[i][k] >= data[i][j]:
                    break

            # walk up; down scenic
            for k in range(i - 1, -1, -1):
                scenic[i][j][1] += 1
                if data[k][j] >= data[i][j]:
                    break

            # walk down; up scenic
            for k in range(i + 1, len(data)):
                scenic[i][j][0] += 1
                if data[k][j] >= data[i][j]:
                    break

    max_scenic = 0
    # max total scenic
    for i in range(len(scenic)):
        for j in range(len(scenic[i])):
            max_scenic = max(max_scenic, reduce(mul, scenic[i][j], 1))

    return max_scenic


def day8_b():
    data = parse_day8_a()
    print("day8_b = {}".format(find_highest_scenic_score(data)))
