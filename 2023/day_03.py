from icecream import ic
from utils.io import read_input

query = read_input('input/day_03.txt')


lines = query.split('\n')


def find_neighbours(i, j):
    sides_to_find = get_sides_to_find(i, j)
    for side in sides_to_find.values():
        x, y = side
        neighbour = lines[x][y]
        if not neighbour.isalnum() and neighbour != '.':
            # ic(True)
            return True
    # ic(False)
    return False


def get_sides_to_find(i, j):
    sides_to_find = {'left': (i, j - 1),
                     'right': (i, j + 1),
                     'up': (i - 1, j),
                     'down': (i + 1, j),
                     'left_up': (i - 1, j - 1),
                     'right_up': (i - 1, j + 1),
                     'right_down': (i + 1, j + 1),
                     'left_down': (i + 1, j - 1)
                     }
    sides_to_remove = set()
    if i == 0:
        sides_to_remove.update(['left_up', 'up', 'right_up'])
    if j == 0:
        sides_to_remove.update(['left_up', 'left', 'left_down'])
    if i >= len(lines) - 1:
        sides_to_remove.update(['left_down', 'down', 'right_down'])
    if j >= len(lines[0]) - 1:
        sides_to_remove.update(['right_up', 'right', 'right_down'])
    for side in sides_to_remove:
        sides_to_find.pop(side, None)
    # ic(sides_to_find)
    return sides_to_find


def gear_ratios(lines):
    result = []
    for i, row in enumerate(lines):
        number = ''
        is_valid = False
        for j, symb in enumerate(row):
            if symb.isdigit():
                number += symb
                if find_neighbours(i, j):
                    is_valid = True
                if j == len(row) - 1 and number != '' and is_valid:
                    result.append(number)
                    is_valid = False
            else:
                if is_valid:
                    result.append(number)
                    is_valid = False
                number = ''
    return sum([int(i) for i in result])


assert gear_ratios(lines) == 532331
