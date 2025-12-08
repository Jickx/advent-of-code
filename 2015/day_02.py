from utils.io import read_lines


def caculate_wrap_area(sizes: list) -> int:
    l, w, h = map(int, sizes)
    side1 = l * w
    side2 = w * h
    side3 = h * l
    min_area_side = min(side1, side2, side3)
    cube_area = sum([2 * side1, 2 * side2, 2 * side3])
    return cube_area + min_area_side


def calculate_ribbon_length(sizes: list) -> int:
    sizes = list(map(int, sizes))
    max_size = max(sizes)
    sizes.remove(max_size)
    return 2 * sum(sizes)


def calculate_bow_length(sizes: list) -> int:
    l, h, w = map(int, sizes)
    return l * h * w


def wrapping_part_1(lines: list) -> int:
    overall_area = 0
    for line in lines:
        area = caculate_wrap_area(line.split("x"))
        overall_area += area
    return overall_area


def wrapping_part_2(lines: list) -> int:
    overall_length = 0
    for line in lines:
        ribbon_length = calculate_ribbon_length(line[::].split("x"))
        bow_length = calculate_bow_length(line[::].split("x"))
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
