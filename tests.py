import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import unittest
from parameterized import parameterized
from collections import deque


class Day1(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             [1000, 2000, 3000],
             [4000],
             [5000, 6000],
             [7000, 8000, 9000],
             [10000]
         ], 24000),
        ("day_1a",
         day1.parse_day1_a(), 69693)
    ])
    def test_find_highest_calories_amount(self, _, data, expected):
        self.assertEqual(expected, day1.find_highest_calories_amount(data))

    @parameterized.expand([
        ("example 2",
         [
             [1000, 2000, 3000],
             [4000],
             [5000, 6000],
             [7000, 8000, 9000],
             [10000]
         ], 45000),
        ("day_1b",
         day1.parse_day1_a(), 200945)
    ])
    def test_find_the_sum_of_top_three(self, _, data, expected):
        self.assertEqual(expected, day1.find_the_sum_of_top_three(data))


class Day2(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             (day2.ROCK, day2.PAPER_PLY),
             (day2.PAPER, day2.ROCK_PLY),
             (day2.SCISSORS, day2.SCISSORS_PLY)
         ], 15),
        ("day_2a",
         day2.parse_day2_a(), 14375)
    ])
    def test_calculate_total_score(self, _, data, expected):
        self.assertEqual(expected, day2.calculate_total_score(data))

    @parameterized.expand([
        ("example 1",
         [
             (day2.ROCK, day2.DRAW),
             (day2.PAPER, day2.LOSE),
             (day2.SCISSORS, day2.WIN)
         ], 12),
        ("day_2b",
         day2.parse_day2_a(), 10274)
    ])
    def test_calculate_total_score_v2(self, _, data, expected):
        self.assertEqual(expected, day2.calculate_total_score_v2(data))


class Day3(unittest.TestCase):
    @parameterized.expand([
        ("example 1", [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
         ], 157),
        ("day_3a",
         day3.parse_day3_a(), 8072)
    ])
    def test_calculate_sum_of_priorities(self, _, data, expected):
        self.assertEqual(expected, day3.calculate_sum_of_priorities(data))

    @parameterized.expand([
        ("example 1", [
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg"
            ],
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw"
            ]
         ], 70),
        ("day_3b",
         day3.parse_day3_b(), 2567)
    ])
    def test_calculate_sum_of_priorities_b(self, _, data, expected):
        self.assertEqual(expected, day3.calculate_sum_of_priorities_b(data))


class Day4(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
            ((6, 6), (4, 6)),
            ((2, 6), (4, 8))
        ), 2),
        ("day_4a",
         day4.parse_day4_a(), 538)
    ])
    def test_count_ranges_fully_overlapping(self, _, data, expected):
        self.assertEqual(expected, day4.count_ranges_fully_overlapping(data))

    @parameterized.expand([
        ("example 1", (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
            ((6, 6), (4, 6)),
            ((2, 6), (4, 8))
        ), 4),
        ("day_4b",
         day4.parse_day4_a(), 792)
    ])
    def test_count_ranges_overlapping(self, _, data, expected):
        self.assertEqual(expected, day4.count_ranges_overlapping(data))


class Day5(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
                (
                    [
                        ['Z', 'N'],
                        ['M', 'C', 'D'],
                        ['P']
                    ],
                    (
                            # (amount, from, to)
                            (1, 2, 1),
                            (3, 1, 3),
                            (2, 2, 1),
                            (1, 1, 2)
                    )
                )
        ), "CMZ"),
        ("day_5a",
         day5.parse_day5_a(), "RLFNRTNFB")
    ])
    def test_find_top_crates(self, _, data, expected):
        self.assertEqual(expected, day5.find_top_crates(data))

    @parameterized.expand([
        ("example 1", (
                (
                    [
                        ['Z', 'N'],
                        ['M', 'C', 'D'],
                        ['P']
                    ],
                    (
                            # (amount, from, to)
                            (1, 2, 1),
                            (3, 1, 3),
                            (2, 2, 1),
                            (1, 1, 2)
                    )
                )
        ), "MCD"),
        ("day_5b",
         day5.parse_day5_a(), "MHQTLJRLB")
    ])
    def test_find_top_crates_FIFO(self, _, data, expected):
        self.assertEqual(expected, day5.find_top_crates_fifo(data))


class Day6(unittest.TestCase):
    @parameterized.expand([
        ("example 1", "bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("example 2", "nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("example 3", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("example 4", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ("day_6a",
         day6.parse_day6_a(), 1262)
    ])
    def test_count_chars_needed_to_detect_marker(self, _, data, expected):
        self.assertEqual(expected, day6.count_chars_needed_to_detect_marker(data, 4))

    @parameterized.expand([
        ("example 1", "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("example 2", "bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("example 3", "nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("example 4", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("example 5", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        # ("day_6b",
        #  day6.parse_day6_a(), 1262)
    ])
    def test_count_chars_needed_to_detect_message(self, _, data, expected):
        self.assertEqual(expected, day6.count_chars_needed_to_detect_marker(data, 14))


class Day7(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"
        ), 95437),
        ("day_7a",
         day7.parse_day7_a(), 1915606)
    ])
    def test_sum_of_dir_sizes(self, _, data, expected):
        self.assertEqual(expected, day7.sum_of_dir_sizes(data))

    @parameterized.expand([
        ("example 1", (
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"
        ), 24933642),
        ("day_7b",
         day7.parse_day7_a(), 5025657)
    ])
    def test_find_size_of_smallest_dir_to_remove(self, _, data, expected):
        self.assertEqual(expected, day7.find_size_of_smallest_dir_to_remove(data))


class Day8(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]
        ), 21),
        ("day_8a",
         day8.parse_day8_a(), 1805)
    ])
    def test_count_visible_trees(self, _, data, expected):
        self.assertEqual(expected, day8.count_visible_trees(data))

    @parameterized.expand([
        ("example 1", (
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]
        ), 8),
        ("day_8b",
         day8.parse_day8_a(), 444528)
    ])
    def test_find_highest_scenic_score(self, _, data, expected):
        self.assertEqual(expected, day8.find_highest_scenic_score(data))


class Day9(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
            ("R", 4),
            ("U", 4),
            ("L", 3),
            ("D", 1),
            ("R", 4),
            ("D", 1),
            ("L", 5),
            ("R", 2)
        ), day9.NO_OF_KNOTS_A, 13),
        ("day_9a", day9.parse_day9_a(), day9.NO_OF_KNOTS_A, 5779),
        ("example 1b", (
                ("R", 5),
                ("U", 8),
                ("L", 8),
                ("D", 3),
                ("R", 17),
                ("D", 10),
                ("L", 25),
                ("U", 20)
        ), day9.NO_OF_KNOTS_B, 36),
        ("example 2b", (
                ("R", 4),
                ("U", 4),
                ("L", 3),
                ("D", 1),
                ("R", 4),
                ("D", 1),
                ("L", 5),
                ("R", 2)
        ), day9.NO_OF_KNOTS_B, 1),
        ("day_9b", day9.parse_day9_a(), day9.NO_OF_KNOTS_B, 2331)
    ])
    def test_count_places_visited_by_tail(self, _, data, no_of_knots, expected):
        self.assertEqual(expected, day9.count_places_visited_by_tail(data, no_of_knots))


class Day10(unittest.TestCase):
    @parameterized.expand([
        ("example 1", (
            ["addx", "15"],
            ["addx", "-11"],
            ["addx", "6"],
            ["addx", "-3"],
            ["addx", "5"],
            ["addx", "-1"],
            ["addx", "-8"],
            ["addx", "13"],
            ["addx", "4"],
            ["noop"],
            ["addx", "-1"],
            ["addx", "5"],
            ["addx", "-1"],
            ["addx", "5"],
            ["addx", "-1"],
            ["addx", "5"],
            ["addx", "-1"],
            ["addx", "5"],
            ["addx", "-1"],
            ["addx", "-35"],
            ["addx", "1"],
            ["addx", "24"],
            ["addx", "-19"],
            ["addx", "1"],
            ["addx", "16"],
            ["addx", "-11"],
            ["noop"],
            ["noop"],
            ["addx", "21"],
            ["addx", "-15"],
            ["noop"],
            ["noop"],
            ["addx", "-3"],
            ["addx", "9"],
            ["addx", "1"],
            ["addx", "-3"],
            ["addx", "8"],
            ["addx", "1"],
            ["addx", "5"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "-36"],
            ["noop"],
            ["addx", "1"],
            ["addx", "7"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "2"],
            ["addx", "6"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "1"],
            ["noop"],
            ["noop"],
            ["addx", "7"],
            ["addx", "1"],
            ["noop"],
            ["addx", "-13"],
            ["addx", "13"],
            ["addx", "7"],
            ["noop"],
            ["addx", "1"],
            ["addx", "-33"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "2"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "8"],
            ["noop"],
            ["addx", "-1"],
            ["addx", "2"],
            ["addx", "1"],
            ["noop"],
            ["addx", "17"],
            ["addx", "-9"],
            ["addx", "1"],
            ["addx", "1"],
            ["addx", "-3"],
            ["addx", "11"],
            ["noop"],
            ["noop"],
            ["addx", "1"],
            ["noop"],
            ["addx", "1"],
            ["noop"],
            ["noop"],
            ["addx", "-13"],
            ["addx", "-19"],
            ["addx", "1"],
            ["addx", "3"],
            ["addx", "26"],
            ["addx", "-30"],
            ["addx", "12"],
            ["addx", "-1"],
            ["addx", "3"],
            ["addx", "1"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "-9"],
            ["addx", "18"],
            ["addx", "1"],
            ["addx", "2"],
            ["noop"],
            ["noop"],
            ["addx", "9"],
            ["noop"],
            ["noop"],
            ["noop"],
            ["addx", "-1"],
            ["addx", "2"],
            ["addx", "-37"],
            ["addx", "1"],
            ["addx", "3"],
            ["noop"],
            ["addx", "15"],
            ["addx", "-21"],
            ["addx", "22"],
            ["addx", "-6"],
            ["addx", "1"],
            ["noop"],
            ["addx", "2"],
            ["addx", "1"],
            ["noop"],
            ["addx", "-10"],
            ["noop"],
            ["noop"],
            ["addx", "20"],
            ["addx", "1"],
            ["addx", "2"],
            ["addx", "2"],
            ["addx", "-6"],
            ["addx", "-11"],
            ["noop"],
            ["noop"],
            ["noop"]
        ), 13140),
        ("day_10a", day10.parse_day10_a(), 15260)
    ])
    def test_calc_sum_of_signal_strengths(self, _, data, expected):
        self.assertEqual(expected, day10.calc_sum_of_signal_strengths(data))

    @parameterized.expand([
        ("example 1", (
                ["addx", "15"],
                ["addx", "-11"],
                ["addx", "6"],
                ["addx", "-3"],
                ["addx", "5"],
                ["addx", "-1"],
                ["addx", "-8"],
                ["addx", "13"],
                ["addx", "4"],
                ["noop"],
                ["addx", "-1"],
                ["addx", "5"],
                ["addx", "-1"],
                ["addx", "5"],
                ["addx", "-1"],
                ["addx", "5"],
                ["addx", "-1"],
                ["addx", "5"],
                ["addx", "-1"],
                ["addx", "-35"],
                ["addx", "1"],
                ["addx", "24"],
                ["addx", "-19"],
                ["addx", "1"],
                ["addx", "16"],
                ["addx", "-11"],
                ["noop"],
                ["noop"],
                ["addx", "21"],
                ["addx", "-15"],
                ["noop"],
                ["noop"],
                ["addx", "-3"],
                ["addx", "9"],
                ["addx", "1"],
                ["addx", "-3"],
                ["addx", "8"],
                ["addx", "1"],
                ["addx", "5"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "-36"],
                ["noop"],
                ["addx", "1"],
                ["addx", "7"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "2"],
                ["addx", "6"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "1"],
                ["noop"],
                ["noop"],
                ["addx", "7"],
                ["addx", "1"],
                ["noop"],
                ["addx", "-13"],
                ["addx", "13"],
                ["addx", "7"],
                ["noop"],
                ["addx", "1"],
                ["addx", "-33"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "2"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "8"],
                ["noop"],
                ["addx", "-1"],
                ["addx", "2"],
                ["addx", "1"],
                ["noop"],
                ["addx", "17"],
                ["addx", "-9"],
                ["addx", "1"],
                ["addx", "1"],
                ["addx", "-3"],
                ["addx", "11"],
                ["noop"],
                ["noop"],
                ["addx", "1"],
                ["noop"],
                ["addx", "1"],
                ["noop"],
                ["noop"],
                ["addx", "-13"],
                ["addx", "-19"],
                ["addx", "1"],
                ["addx", "3"],
                ["addx", "26"],
                ["addx", "-30"],
                ["addx", "12"],
                ["addx", "-1"],
                ["addx", "3"],
                ["addx", "1"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "-9"],
                ["addx", "18"],
                ["addx", "1"],
                ["addx", "2"],
                ["noop"],
                ["noop"],
                ["addx", "9"],
                ["noop"],
                ["noop"],
                ["noop"],
                ["addx", "-1"],
                ["addx", "2"],
                ["addx", "-37"],
                ["addx", "1"],
                ["addx", "3"],
                ["noop"],
                ["addx", "15"],
                ["addx", "-21"],
                ["addx", "22"],
                ["addx", "-6"],
                ["addx", "1"],
                ["noop"],
                ["addx", "2"],
                ["addx", "1"],
                ["noop"],
                ["addx", "-10"],
                ["noop"],
                ["noop"],
                ["addx", "20"],
                ["addx", "1"],
                ["addx", "2"],
                ["addx", "2"],
                ["addx", "-6"],
                ["addx", "-11"],
                ["noop"],
                ["noop"],
                ["noop"]
        ), [
            "##..##..##..##..##..##..##..##..##..##..",
            "###...###...###...###...###...###...###.",
            "####....####....####....####....####....",
            "#####.....#####.....#####.....#####.....",
            "######......######......######......####",
            "#######.......#######.......#######....."
        ]),
        ("day_10b", day10.parse_day10_a(),
            [
                "###...##..#..#.####..##..#....#..#..##..",
                "#..#.#..#.#..#.#....#..#.#....#..#.#..#.",
                "#..#.#....####.###..#....#....#..#.#....",
                "###..#.##.#..#.#....#.##.#....#..#.#.##.",
                "#....#..#.#..#.#....#..#.#....#..#.#..#.",
                "#.....###.#..#.#.....###.####..##...###."
            ])
    ])
    def test_draw_screen(self, _, data, expected):
        self.assertEqual(expected, day10.draw_screen(data))


class Day11(unittest.TestCase):
    @parameterized.expand([
        ("example 1", [
            day11.Monkey(0, deque([79, 98]), ("*", 19), (23, 3, 2)),
            day11.Monkey(1, deque([54, 65, 75, 74]), ("+", 6), (19, 0, 2)),
            day11.Monkey(2, deque([79, 60, 97]), ("*", "old"), (13, 3, 1)),
            day11.Monkey(3, deque([74]), ("+", 3), (17, 1, 0)),
        ], 20, 3, 10605),
        ("day_11a",
         day11.parse_day11_a(), 20, 3, 182293),
        ("example 2", [
            day11.Monkey(0, deque([79, 98]), ("*", 19), (23, 3, 2)),
            day11.Monkey(1, deque([54, 65, 75, 74]), ("+", 6), (19, 0, 2)),
            day11.Monkey(2, deque([79, 60, 97]), ("*", "old"), (13, 3, 1)),
            day11.Monkey(3, deque([74]), ("+", 3), (17, 1, 0)),
        ], 10000, 23 * 19 * 17 * 13, 2713310158),
        ("day_11b",
         day11.parse_day11_a(), 10000, 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19,  54832778815)
    ])
    def test_calc_level_of_monkey_business(self, _, data, num_of_rounds, worry_divisor, expected):
        self.assertEqual(expected, day11.calc_level_of_monkey_business(data, num_of_rounds, worry_divisor))


class Day12(unittest.TestCase):
    @parameterized.expand([
        ("example 1", [
            [0, 0, 1, 16, 15, 14, 13, 12],
            [0, 1, 2, 17, 24, 23, 23, 11],
            [0, 2, 2, 18, 25, 25, 23, 10],
            [0, 2, 2, 19, 20, 21, 22, 9],
            [0, 1, 3, 4, 5, 6, 7, 8]
        ], (0, 0), (2, 5), 31),
        ("example 2", [
            [0, 1, 2, 16, 15, 14, 13, 12],
            [0, 1, 0, 17, 24, 23, 23, 11],
            [0, 2, 1, 18, 25, 25, 23, 10],
            [0, 2, 2, 19, 20, 21, 22, 9],
            [0, 1, 3, 4, 5, 6, 7, 8]
        ], (0, 0), (2, 5), 31),
        ("day_12a",
         day12.parse_day12_a()[0], day12.parse_day12_a()[1], day12.parse_day12_a()[2], 391)
    ])
    def test_find_shortest_path(self, _, data, src, trgt, expected):
        self.assertEqual(expected, day12.find_shortest_path(data, src, trgt))

    @parameterized.expand([
        ("example 1", [
            [0, 0, 1, 16, 15, 14, 13, 12],
            [0, 1, 2, 17, 24, 23, 23, 11],
            [0, 2, 2, 18, 25, 25, 23, 10],
            [0, 2, 2, 19, 20, 21, 22, 9],
            [0, 1, 3, 4, 5, 6, 7, 8]
        ], (2, 5), 29),

        ("day_12b",
         day12.parse_day12_a()[0], day12.parse_day12_a()[2], 386)
    ])
    def test_find_shortest_path(self, _, data, src, expected):
        self.assertEqual(expected, day12.find_shortest_path_from_any_a(data, src))


class Day13(unittest.TestCase):
    @parameterized.expand([
        ("own 1",
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
            -1),
        ("own 2",
            [1],
            [1],
            0),
        ("own 3",
            [2],
            [1],
            1),
        ("own 4",
            [1, [1]],
            [1, 1],
            0),
        ("own 5",
         [1, 1],
         [1, [1]],
         0),
        ("own 6",
         [1, [1]],
         [1],
         1),
        ("own 7",
         [1, [1, 2, 3, 4]],
         [1, [1, 2, 3, [4]]],
         0),
    ])
    def test_compare(self, _, a, b, expected):
        self.assertEqual(expected, day13.compare(a, b))

    @parameterized.expand([
        ("example 1", [
            [
                [1, 1, 3, 1, 1],
                [1, 1, 5, 1, 1]
            ],

            [
                [[1], [2, 3, 4]],
                [[1], 4]
            ],

            [
                [9],
                [[8, 7, 6]]
            ],

            [
                [[4, 4], 4, 4],
                [[4, 4], 4, 4, 4]
            ],

            [
                [7, 7, 7, 7],
                [7, 7, 7]
            ],

            [
                [],
                [3]
            ],

            [
                [[[]]],
                [[]]
            ],

            [
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
            ]
        ], 13),

        ("day_13a",
         day13.parse_day13_a(), 5003)
    ])
    def test_sum_of_indices(self, _, data, expected):
        self.assertEqual(expected, day13.sum_of_indices(data))

    @parameterized.expand([
        ("example 1", [
            [
                [1, 1, 3, 1, 1],
                [1, 1, 5, 1, 1]
            ],

            [
                [[1], [2, 3, 4]],
                [[1], 4]
            ],

            [
                [9],
                [[8, 7, 6]]
            ],

            [
                [[4, 4], 4, 4],
                [[4, 4], 4, 4, 4]
            ],

            [
                [7, 7, 7, 7],
                [7, 7, 7]
            ],

            [
                [],
                [3]
            ],

            [
                [[[]]],
                [[]]
            ],

            [
                [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
            ]
        ], 140),

        ("day_13b",
         day13.parse_day13_a(), 20280)
    ])
    def test_sum_of_indices(self, _, data, expected):
        self.assertEqual(expected, day13.find_decoder_key(data))


class Day14(unittest.TestCase):
    @parameterized.expand([
        ("example 1", [
            [(498, 4), (498, 6), (496, 6)],
            [(503, 4), (502, 4), (502, 9), (494, 9)]
        ], 24),
        ("day_14a", day14.parse_day14_a(), 892)
    ])
    def test_count_units_of_sand_until_fall(self, _, data, expected):
        self.assertEqual(expected, day14.count_units_of_sand_until_fall(data))

    @parameterized.expand([
        ("example 1", [
            [(498, 4), (498, 6), (496, 6)],
            [(503, 4), (502, 4), (502, 9), (494, 9)]
        ], 93),
        ("day_14b", day14.parse_day14_a(), 27155)
    ])
    def test_count_units_of_sand_untin_blockage(self, _, data, expected):
        self.assertEqual(expected, day14.count_units_of_sand_until_blockage(data))


class Day15(unittest.TestCase):
    @parameterized.expand([
        ("example 1", [
            ((2, 18), (-2, 15)),
            ((9, 16), (10, 16)),
            ((13, 2), (15, 3)),
            ((12, 14), (10, 16)),

            ((10, 20), (10, 16)),
            ((14, 17), (10, 16)),
            ((8, 7), (2, 10)),
            ((2, 0), (2, 10)),

            ((0, 11), (2, 10)),
            ((20, 14), (25, 17)),
            ((17, 20), (21, 22)),
            ((16, 7), (15, 3)),

            ((14, 3), (15, 3)),
            ((20, 1), (15, 3)),
        ], 10, 26),
        ("day_15a", day15.parse_day15_a(), 2000000, 5832528)
    ])
    def test_count_positions_without_beacon(self, _, data, row, expected):
        self.assertEqual(expected, day15.count_positions_without_beacon(data, row))

    @parameterized.expand([
        ("example 1", [
            ((2, 18), (-2, 15)),
            ((9, 16), (10, 16)),
            ((13, 2), (15, 3)),
            ((12, 14), (10, 16)),

            ((10, 20), (10, 16)),
            ((14, 17), (10, 16)),
            ((8, 7), (2, 10)),
            ((2, 0), (2, 10)),

            ((0, 11), (2, 10)),
            ((20, 14), (25, 17)),
            ((17, 20), (21, 22)),
            ((16, 7), (15, 3)),

            ((14, 3), (15, 3)),
            ((20, 1), (15, 3)),
        ], 20, 56000011),
        ("day_15b", day15.parse_day15_a(), 4000000, 13360899249595)
    ])
    def test_tuning_frequency(self, _, data, bounds, expected):
        self.assertEqual(expected, day15.tuning_frequency(data, bounds))
