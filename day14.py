from utilities import non_blank_lines
import math


def parse_day14_a():
    with open("day14.txt", "r") as f:
        data = [[eval(x) for x in line.split(" -> ")] for line in non_blank_lines(f)]

    return data


def draw_paths(data):
    rock = set()
    max_y = [0 for _ in range(600)]

    for path in data:
        for i in range(len(path) - 1):
            x0, y0 = path[i]
            x1, y1 = path[i + 1]
            dx = x1 - x0
            dy = y1 - y0

            if dx != 0:
                step = int(math.copysign(1, dx))
                for j in range(x0, x1 + step, step):
                    rock.add((j, y0))
                    max_y[j] = max(max_y[j], y0)

            else:
                step = int(math.copysign(1, dy))
                for j in range(y0, y1 + step, step):
                    rock.add((x0, j))

                max_y[x0] = max(max_y[x0], y1)

    return rock, max_y


def count_units_of_sand_until_fall(data):
    rock, max_y = draw_paths(data)
    sand_src = (500, 0)
    inf = False
    ans = 0

    while not inf:
        x, y = sand_src
        move_avail = True
        ans += 1

        while move_avail:
            if (x, y + 1) not in rock:
                y += 1
            elif (x - 1, y + 1) not in rock:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rock:
                y += 1
                x += 1
            else:
                rock.add((x, y))
                move_avail = False

            if move_avail:
                if y > max_y[x]:
                    inf = True
                    break

    return ans - 1


def day14_a():
    data = parse_day14_a()
    print("day14_a = {}".format(count_units_of_sand_until_fall(data)))


def count_units_of_sand_until_blockage(data):
    rock, max_y = draw_paths(data)
    floor_y = 2 + max(max_y)
    sand_src = (500, 0)
    ans = 0

    while sand_src not in rock:
        x, y = sand_src
        move_avail = True
        while move_avail:
            if y == floor_y - 1:
                rock.add((x, y))
                move_avail = False
            elif (x, y + 1) not in rock:
                y += 1
            elif (x - 1, y + 1) not in rock:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rock:
                y += 1
                x += 1
            else:
                rock.add((x, y))
                move_avail = False

        ans += 1

    return ans


def day14_b():
    data = parse_day14_a()
    print("day14_b = {}".format(count_units_of_sand_until_blockage(data)))
