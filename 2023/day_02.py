"""
Advent of Code 2023 - Day 02 (https://adventofcode.com/2023/day/2)
"""
from collections import defaultdict
from utils.io import read_lines

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def is_set_valid(sets):
    for _set in sets:
        cubes = _set.split(',')
        for cube in cubes:
            cubes_split = cube.strip(' ').split(' ')
            cubes_num, cubes_color = cubes_split[0], cubes_split[1]
            if int(cubes_num) > MAX_CUBES[cubes_color]:
                return False
    return True


def count_games_part_1(data):
    result = 0
    for line in data:
        line_split = line.split(':')
        game_num = line_split[0].split(' ')[1]
        sets = line_split[1].split(';')
        set_valid = is_set_valid(sets)
        if set_valid:
            result += int(game_num)
    return result


def find_fewest_games(sets):
    games_list = []
    for _set in sets:
        cubes_dict = {}
        cubes = _set.split(',')
        for cube in cubes:
            cubes_split = cube.strip(' ').split(' ')
            cubes_num, cubes_color = cubes_split[0], cubes_split[1]
            cubes_dict[cubes_color] = cubes_num
        games_list.append(cubes_dict)

    games_dict = defaultdict(int)
    for game in games_list:
        for k, v in game.items():
            games_dict[k] = max(games_dict[k], int(v))
    result = 1
    for v in games_dict.values():
        result *= int(v)
    return result


def count_games_part_2(data):
    result = 0
    for line in data:
        line_split = line.split(':')
        sets = line_split[1].split(';')
        result += find_fewest_games(sets)
    return result


data = read_lines('input/day_02.txt')

assert count_games_part_1(data) == 2727
assert count_games_part_2(data) == 56580
