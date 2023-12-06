"""
Advent of Code 2023 - Day 01 (https://adventofcode.com/2023/day/1)
"""
import re

query = open('input/day_01.txt', 'r').read()
lines = query.split('\n')

num_str = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def trebuchet_part_1(lines):
    calibration = 0
    for line in lines:
        calibration += int(re.findall(r'\d', line)[0] + re.findall(r'\d', line)[-1])
    return calibration


def trebuchet_part_2(lines):
    calibration = 0
    for line in lines:
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        seq = ''.join([num_str[i] if i.isalpha() else i for i in [digits[0], digits[-1]]])
        calibration += int(seq)
    return calibration


assert trebuchet_part_1(lines) == 54634
assert trebuchet_part_2(lines) == 53855
