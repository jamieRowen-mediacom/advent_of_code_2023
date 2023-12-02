import textwrap
import advent_of_code as aoc

with open("inputs/day_one.txt") as f:
    input = f.read()

print(f"day_one_part_one: {aoc.day_one.part_one(input)}")
print(f"day_one_part_two: {aoc.day_one.part_two(input)}")