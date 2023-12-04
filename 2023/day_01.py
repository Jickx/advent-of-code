"""
Advent of Code 2023 - Day 01 (https://adventofcode.com/2023/day/1)
"""
import re


def trebuchet():
    query = open('input/day_01.txt', 'r').read()
    lines = query.split('\n')
    calibration = 0
    for line in lines:
        calibration += int(re.findall(r'\d', line)[0] + re.findall(r'\d', line)[-1])

    return calibration


assert trebuchet() == 54634
