from utilities import non_blank_lines
import functools


def parse_day13_a():
    data = []
    chunk = []
    with open("day13.txt", "r") as f:
        k = 0
        for line in non_blank_lines(f):
            chunk.append(list(eval(line)))
            k += 1
            if k == 2:
                data.append(chunk.copy())
                chunk.clear()
                k = 0

    return data


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else (1 if a > b else 0)
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            if len(a) != len(b):
                if i >= len(a):
                    return -1
                if i >= len(b):
                    return 1
            ans = compare(a[i], b[i])
            if ans != 0:
                return ans
        return 0
    else:
        if isinstance(a, int):
            return compare([a], b)
        else:
            return compare(a, [b])


def sum_of_indices(data):
    ans = 0

    for i in range(len(data)):
        if compare(data[i][0], data[i][1]) == -1:
            ans += i + 1

    return ans


def find_decoder_key(data):
    packets = [[[2]], [[6]]]
    for a, b in data:
        packets.append(a)
        packets.append(b)

    packets.sort(key=functools.cmp_to_key(compare))

    ans = 1

    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            ans *= i + 1

    return ans


def day13_a():
    data = parse_day13_a()
    print("day13_a = {}".format(sum_of_indices(data)))


def day13_b():
    data = parse_day13_a()
    print("day13_b = {}".format(find_decoder_key(data)))
