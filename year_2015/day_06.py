import re

from utils.io import read_lines


# "·*⦿Ж"


def change_light(light: str, mode: str = None) -> str:
    if mode == 'on':
        return '*'
    elif mode == 'off':
        return '·'
    elif mode == 'toggle' and light == '·':
        return '*'
    elif mode == 'toggle' and light == '*':
        return '·'
    else:
        return light


def change_lights(lights: list[list[str]], mode: str, coords: tuple) -> list[list[str]]:
    (x1, y1), (x2, y2) = coords
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            lights[y][x] = change_light(lights[y][x], mode)
    return lights


def change_brightness(lights, mode, coords):
    (x1, y1), (x2, y2) = coords
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if mode == 'on':
                lights[y][x] += 1
            elif mode == "off":
                brightness = lights[y][x] - 1
                lights[y][x] = max(brightness, 0)
            elif mode == "toggle":
                lights[y][x] += 2
    return lights


def get_mode(line: str) -> str:
    if "turn on" in line:
        return "on"
    elif "turn off" in line:
        return "off"
    elif "toggle" in line:
        return "toggle"
    else:
        return ''


def get_coordinates(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    (x1, y1), (x2, y2) = re.findall(r"(\d+),(\d+)", line)
    return (int(x1), int(y1)), (int(x2), int(y2))


def write_in_file(lights: list[list[str]]) -> None:
    with open('lights.txt', 'w') as f:
        for row in lights:
            f.write(''.join(row) + '\n')


def count_lights_part_1(lines: list[str]) -> int:
    lights = [['·' for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        mode = get_mode(line)
        coords = get_coordinates(line)
        change_lights(lights, mode, coords)
    # write_in_file(lights)
    return sum(cell == '*' for row in lights for cell in row)


def count_lights_part_2(lines: list[str]) -> int:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        mode = get_mode(line)
        coords = get_coordinates(line)
        change_brightness(lights, mode, coords)
    return sum(num for row in lights for num in row)


if __name__ == "__main__":
    input_lines = read_lines("input/day_06.txt")
    print(count_lights_part_1(input_lines))
    print(count_lights_part_2(input_lines))


