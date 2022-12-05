import day1
import day2
import day3
import day4
import day5
import unittest
from parameterized import parameterized


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
