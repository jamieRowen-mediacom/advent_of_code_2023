import re
from functools import reduce

def parse_game(x: str):
    if len(x) == 0: return None
    id = int(re.findall("(Game) (\\d+):", x)[0][1])
    draws = []
    for y in x.split(";"):
        draws.append({
            col: int(num) for num, col in re.findall("(\\d+) (red|green|blue)", y)
        })
    return {
        "id": id,
        "draws": draws
    }

def possible_game(x, available):
    if x is None: return None
    return all([draw.get("green", 0) <= available["green"] and  draw.get("red", 0) <= available["red"] and draw.get("blue", 0) <= available["blue"] for draw in x["draws"]])

def part_one(input: str, available = {}):
    """
    You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

    The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

    As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

    To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

    You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

    For example, the record of a few games might look like this:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

    The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

    In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
    """
    if not available:
        available = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
    return sum(
        map(
            lambda x: x["id"],
            filter(lambda x: possible_game(x, available), [parse_game(x) for x in input.split("\n")])
        )
    )


def power(x):
    if x is None: return 0
    vals = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for draw in x["draws"]:
        vals["red"] = max(draw.get("red", 0), vals["red"])
        vals["green"] = max(draw.get("green", 0), vals["green"])
        vals["blue"] = max(draw.get("blue", 0), vals["blue"])
    return reduce(lambda x, y: x * y, vals.values(), 1)

def part_two(input):
    return sum([power(parse_game(x)) for x in input.split("\n")])