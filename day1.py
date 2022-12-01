

def parse_day1_a():
    with open("day1.txt", "r") as f:
        raw_data = list(f.read().splitlines())

    data = []
    chunk = []
    for x in raw_data:
        if not len(x) == 0:
            chunk.append(int(x))
        else:
            data.append(chunk[:])
            chunk.clear()

    return data


def find_highest_calories_amount(elves_list):
    return max([sum(elve) for elve in elves_list])


def day1_a():
    data = parse_day1_a()
    print("day1_a = {}".format(find_highest_calories_amount(data)))


def find_the_sum_of_top_three(elves_list):
    return sum(sorted([sum(elve) for elve in elves_list], reverse=True)[0:3])


def day1_b():
    data = parse_day1_a()
    print("day1_b = {}".format(find_the_sum_of_top_three(data)))
