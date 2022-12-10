from utilities import non_blank_lines


def parse_day10_a():
    with open("day10.txt", "r") as f:
        data = [line.split() for line in non_blank_lines(f)]

    return tuple(data)


def calc_sum_of_signal_strengths(data):
    x = 1
    cycles = 1
    x_vals = dict()

    for cmd in data:
        x_vals[cycles] = x
        if cmd[0] == "noop":
            cycles += 1
        else:
            c, a = cmd
            cycles += 1
            x_vals[cycles] = x
            cycles += 1
            x += int(a)

    return sum([k * v for k, v in x_vals.items() if k in (20, 60, 100, 140, 180, 220)])


def day10_a():
    data = parse_day10_a()
    print("day10_a = {}".format(calc_sum_of_signal_strengths(data)))


def draw_screen(data):
    x = 1
    cycles = 0
    screen = []
    curr_line = ""

    for cmd in data:
        # x_vals[cycles] = x
        if cycles % 40 in (x - 1, x, x + 1):
            curr_line += "#"
        else:
            curr_line += "."
        if len(curr_line) % 40 == 0:
            screen.append(curr_line)
            curr_line = ""

        if cmd[0] == "noop":
            cycles += 1
        else:
            c, a = cmd
            cycles += 1
            # x_vals[cycles] = x
            if cycles % 40 in (x - 1, x, x + 1):
                curr_line += "#"
            else:
                curr_line += "."
            if len(curr_line) % 40 == 0:
                screen.append(curr_line)
                curr_line = ""

            cycles += 1
            x += int(a)

    # print(curr_line)
    for x in screen:
        print(x)

    return screen


def day10_b():
    data = parse_day10_a()
    print("day10_b = {}".format(draw_screen(data)))
