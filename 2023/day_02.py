"""
Advent of Code 2023 - Day 02 (https://adventofcode.com/2023/day/2)
"""

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def is_set_valid(cubes_set):
    for _set in cubes_set:
        cubes = _set.split(',')
        for cube in cubes:
            cubes_split = cube.strip(' ').split(' ')
            cubes_num, cubes_color = cubes_split[0], cubes_split[1]
            if int(cubes_num) > MAX_CUBES[cubes_color]:
                return False
    return True


def count_games():
    with open('input/day_02.txt', 'r') as f:
        data = []
        for line in f:
            data.append(line.strip('\n'))

    data_dict = {}
    result = 0
    for line in data:
        line_split = line.split(':')
        game_num = line_split[0].split(' ')[1]
        sets = line_split[1].split(';')
        set_valid = is_set_valid(sets)
        if set_valid:
            result += int(game_num)

    return result


print(count_games())
