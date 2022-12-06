from utilities import non_blank_lines

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

ROCK_PLY = "X"
PAPER_PLY = "Y"
SCISSORS_PLY = "Z"

LOSE = "X"
DRAW = "Y"
WIN = "Z"

shape_points = {
    ROCK_PLY: 1,
    PAPER_PLY: 2,
    SCISSORS_PLY: 3
}


def parse_day2_a():
    with open("day2.txt", "r") as f:
        data = [(line.split()[0], line.split()[1]) for line in non_blank_lines(f)]
        # print(data)

    return data


def calculate_total_score(data):
    match_points = {
        (ROCK, ROCK_PLY): 3,
        (ROCK, PAPER_PLY): 6,
        (ROCK, SCISSORS_PLY): 0,

        (PAPER, ROCK_PLY): 0,
        (PAPER, PAPER_PLY): 3,
        (PAPER, SCISSORS_PLY): 6,

        (SCISSORS, ROCK_PLY): 6,
        (SCISSORS, PAPER_PLY): 0,
        (SCISSORS, SCISSORS_PLY): 3,
    }

    return sum([match_points[x] + shape_points[x[1]] for x in data])



def day2_a():
    data = parse_day2_a()
    print("day2_a = {}".format(calculate_total_score(data)))

def calculate_total_score_v2(data):
    match_strategy = {
        (ROCK, LOSE): SCISSORS_PLY,
        (ROCK, DRAW): ROCK_PLY,
        (ROCK, WIN): PAPER_PLY,

        (PAPER, LOSE): ROCK_PLY,
        (PAPER, DRAW): PAPER_PLY,
        (PAPER, WIN): SCISSORS_PLY,

        (SCISSORS, LOSE): PAPER_PLY,
        (SCISSORS, DRAW): SCISSORS_PLY,
        (SCISSORS, WIN): ROCK_PLY
    }

    match_result_points = {
        LOSE: 0,
        DRAW: 3,
        WIN: 6
    }

    result = 0

    for x in data:
        result += match_result_points[x[1]] + shape_points[match_strategy[x]]

    return result


def day2_b():
    data = parse_day2_a()
    print("day1_b = {}".format(calculate_total_score_v2(data)))
