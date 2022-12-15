from utilities import non_blank_lines
import re


def parse_day15_a():
    with open("day15.txt", "r") as f:
        splitted_data = [re.split("[ =,:]", line) for line in non_blank_lines(f)]

    return [((int(line[3]), int(line[6])), (int(line[13]), int(line[16]))) for line in splitted_data]


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def count_positions_without_beacon(data, row):
    empty = set()
    beacons = set()

    for s, b in data:
        beacons.add(b)
        m = manhattan(s, b)
        sx, sy = s

        for x in range(-(m - abs(row - sy)), (m - abs(row - sy)) + 1):
            empty.add((sx + x, row))

    cnt = 0
    for x, y in empty:
        if y == row and (x, y) not in beacons:
            cnt += 1

    return cnt


def day15_a():
    data = parse_day15_a()
    print("day15_a = {}".format(count_positions_without_beacon(data, row=2000000)))


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])

    idx = 0

    for i in range(1, len(ranges)):
        if ranges[idx][1] >= ranges[i][0] - 1:
            ranges[idx][1] = max(ranges[idx][1], ranges[i][1])
        else:
            idx = idx + 1
            ranges[idx] = ranges[i]

    return ranges[:idx + 1]


def tuning_frequency(data, bounds):
    manhattans = {}

    for s, b in data:
        manhattans[s] = manhattan(s, b)

    for y in range(bounds, -1, -1):
        ranges = []
        for s in manhattans:
            sx, sy = s

            if sy > y >= sy - manhattans[s] or sy <= y <= sy + manhattans[s]:
                dy = abs(sy - y)
                ranges.append([sx - abs(manhattans[s] - dy), sx + abs(manhattans[s] - dy)])

        merged_range = merge_ranges(ranges)
        if len(merged_range) == 2:
            x = merged_range[0][1] + 1
            return x * 4000000 + y


def day15_b():
    data = parse_day15_a()
    print("day15_b = {}".format(tuning_frequency(data, bounds=4000000)))
