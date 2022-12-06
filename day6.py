

def parse_day6_a():
    with open("day6.txt", "r") as f:
        data = list(f.read().splitlines())

    return data[0]


def count_chars_needed_to_detect_marker(data, marker_len):
    n = marker_len
    for i in range(0, len(data) - marker_len):
        if len(set(data[i: i+marker_len])) == marker_len:
            return n
        n += 1

    return -1


def day6_a():
    data = parse_day6_a()
    print("day6_a = {}".format(count_chars_needed_to_detect_marker(data, 4)))


def day6_b():
    data = parse_day6_a()
    print("day6_b = {}".format(count_chars_needed_to_detect_marker(data, 14)))
