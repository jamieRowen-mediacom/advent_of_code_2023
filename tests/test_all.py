import textwrap
import advent_of_code as aoc


def test_day1_a():
    input = textwrap.dedent(
        """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""
    )
    assert aoc.day_one.part_one(input) == 142

def test_day1_b():
    input = textwrap.dedent(
        """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
    )
    assert aoc.day_one.part_two(input) == 281