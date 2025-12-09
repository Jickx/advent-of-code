from utils.io import read_lines


def is_contains_vowel(line: str) -> bool:
    return len([char for char in line if char in "aeiou"]) >= 3


def is_contains_double_letter(line: str) -> bool:
    prev = 0
    for curr in range(1, len(line)):
        if line[prev] == line[curr]:
            return True
        prev += 1
    return False


def is_not_contains_strings(line: str) -> bool:
    strings = ["ab", "cd", "pq", "xy"]
    for string in strings:
        if string in line:
            return False
    return True


def is_contains_pair_of_letters(line: str) -> bool:
    for i in range(1, len(line)):
        if line[i - 1:i + 1] in line[i + 1:]:
            return True
    return False


def is_contains_at_least_one_repeating_letter(line: str) -> bool:
    for i in range(1, len(line) - 1):
        if line[i - 1] == line[i + 1]:
            return True
    return False


def count_nice_strings_part_1(lines: list[str]) -> int:
    cnt = 0
    for line in lines:
        if is_contains_vowel(line) and is_contains_double_letter(line) and is_not_contains_strings(line):
            cnt += 1
    return cnt


def count_nice_strings_part_2(lines: list[str]) -> int:
    cnt = 0
    for line in lines:
        if is_contains_pair_of_letters(line) and is_contains_at_least_one_repeating_letter(line):
            cnt += 1
    return cnt


if __name__ == "__main__":
    lines = read_lines("input/day_05.txt")
    print(count_nice_strings_part_1(lines))
    print(count_nice_strings_part_2(lines))
