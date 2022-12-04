import string
import numpy as np

priorities = dict(zip(string.ascii_letters, range(1, 53)))


def parse_day3_a():
    with open("day3.txt", "r") as f:
        data = list(f.read().splitlines())
    return data


def calculate_sum_of_priorities(data):
    return sum([priorities[''.join(set(x[:len(x) // 2]).intersection(set(x[len(x) // 2:])))] for x in data])


def day3_a():
    data = parse_day3_a()
    print("day3_a = {}".format(calculate_sum_of_priorities(data)))


def parse_day3_b():
    with open("day3.txt", "r") as f:
        data = list(f.read().splitlines())

    chunk_siz = 3
    return [data[i:i + chunk_siz] for i in range(0, len(data), chunk_siz)]


def calculate_sum_of_priorities_b(data):
    return sum([priorities[''.join(set(group[0]).intersection(set(group[1]), group[2]))] for group in data])


def day3_b():
    data = parse_day3_b()
    print("day3_b = {}".format(calculate_sum_of_priorities_b(data)))
