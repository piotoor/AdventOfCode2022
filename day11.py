from utilities import non_blank_lines
from collections import deque
import re


class Monkey:
    def __init__(self, mid, items, operation, test):
        self.mid = mid
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected = 0
        # print("---------- monkey {} ----------".format(self.mid))
        # print("mid = {}".format(mid))
        # print("items = {}".format(items))
        # print("operation = {}".format(operation))
        # print("test = {}".format(test))


def parse_day11_a():
    with open("day11.txt", "r") as f:
        raw_data = [line for line in non_blank_lines(f)]

    data = []
    n = 0
    for m in range(8):
        n += 1
        raw_data[n] = re.sub(",", "", raw_data[n])
        elements = raw_data[n].split()[2:]

        n += 1
        line_split = raw_data[n].split()
        operations = (line_split[-2], line_split[-1] if line_split[-1] == "old" else int(line_split[-1]))

        n += 1
        line_split = raw_data[n].split()
        div = int(line_split[-1])
        n += 1
        line_split = raw_data[n].split()
        true_target = int(line_split[-1])
        n += 1
        line_split = raw_data[n].split()
        false_target = int(line_split[-1])
        monkey = Monkey(m, deque(deque(map(int, elements))), operations, (div, false_target, true_target))
        data.append(monkey)
        n += 1
    return data


def calc_level_of_monkey_business(monkeys, num_of_rounds, worry_divisor):
    for r in range(num_of_rounds):
        for m in monkeys:
            while not len(m.items) == 0:
                m.inspected += 1
                front = m.items.popleft()
                arg = m.operation[1]
                if arg == "old":
                    arg = front

                # operation
                if m.operation[0] == "*":
                    front *= arg
                elif m.operation[0] == "+":
                    front += arg

                # simplification
                if num_of_rounds == 20:
                    front //= worry_divisor
                else:
                    front %= worry_divisor

                # test & throw
                if front % m.test[0] == 0:
                    monkeys[m.test[2]].items.append(front)
                else:
                    monkeys[m.test[1]].items.append(front)

    monkeys.sort(key=lambda a: a.inspected)

    return monkeys[-1].inspected * monkeys[-2].inspected


def day11_a():
    data = parse_day11_a()
    print("day11_a = {}".format(calc_level_of_monkey_business(data, num_of_rounds=20, worry_divisor=3)))


def day11_b():
    data = parse_day11_a()
    print("day11_b = {}".format(calc_level_of_monkey_business(data, num_of_rounds=10000, worry_divisor=2*3*5*7*11*13*17*19)))
