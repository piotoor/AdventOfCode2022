from utilities import non_blank_lines


def parse_day4_a():
    with open("day4.txt", "r") as f:
        data = [(tuple(map(int, line.split(",")[0].split("-"))), tuple(map(int, line.split(",")[1].split("-"))))
                for line in non_blank_lines(f)]

    return tuple(data)


def count_ranges_fully_overlapping(data):
    cnt = 0

    for x, y in data:
        if x[0] >= y[0] and x[1] <= y[1] or x[0] <= y[0] and x[1] >= y[1]:
            cnt += 1

    return cnt


def day4_a():
    data = parse_day4_a()
    print("day4_a = {}".format(count_ranges_fully_overlapping(data)))


def count_ranges_overlapping(data):
    cnt = 0

    for x, y in data:
        if y[0] <= x[0] <= y[1] or y[0] <= x[1] <= y[1] or x[0] <= y[0] <= x[1] or x[0] <= y[1] <= x[1]:
            cnt += 1

    return cnt


def day4_b():
    data = parse_day4_a()
    print("day4_b = {}".format(count_ranges_overlapping(data)))
