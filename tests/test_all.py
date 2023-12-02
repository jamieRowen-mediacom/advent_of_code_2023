import textwrap
import advent_of_code as aoc


def test_day_one_part_one():
    input = textwrap.dedent(
        """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""
    )
    assert aoc.day_one.part_one(input) == 142

def test_day_one_part_two():
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


def test_day_two_part_one():
    input = textwrap.dedent(
        """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
    )
    assert aoc.day_two.part_one(input) == 8


def test_day_two_part_two():
    input = textwrap.dedent(
        """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
    )
    assert aoc.day_two.part_two(input) == 2286