from utils.io import read_lines


def calculate_wrap_area(sizes: list[str]) -> int:
    l, w, h = map(int, sizes)
    side1 = l * w
    side2 = w * h
    side3 = h * l
    min_area_side = min(side1, side2, side3)
    surface_area = 2 * side1 + 2 * side2 + 2 * side3
    return surface_area + min_area_side


def calculate_ribbon_length(sizes: list) -> int:
    a, b, c = sorted(map(int, sizes))
    return 2 * (a + b)


def calculate_bow_length(sizes: list) -> int:
    l, w, h = map(int, sizes)
    return l * w * h


def wrapping_part_1(input_lines: list[str]) -> int:
    overall_area = 0
    for line in input_lines:
        overall_area += calculate_wrap_area(line.split("x"))
    return overall_area


def wrapping_part_2(input_lines: list[str]) -> int:
    overall_length = 0
    for line in input_lines:
        dims = line.split("x")
        ribbon_length = calculate_ribbon_length(dims)
        bow_length = calculate_bow_length(dims)
        overall_length += ribbon_length + bow_length
    return overall_length


def run_tests():
    assert wrapping_part_1(["2x3x4"]) == 58
    assert wrapping_part_2(["2x3x4"]) == 34
    assert wrapping_part_1(["1x1x10"]) == 43
    assert wrapping_part_2(["1x1x10"]) == 14


if __name__ == "__main__":
    run_tests()
    lines = read_lines("input/day_02.txt")
    print(wrapping_part_1(lines))
    print(wrapping_part_2(lines))
