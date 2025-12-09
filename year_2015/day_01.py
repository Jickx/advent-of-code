from utils.io import read_input


def find_floor_part_1(sequence: str) -> int:
    floor = 0
    for ch in sequence:
        if ch == "(":
            floor += 1
        elif ch == ")":
            floor -= 1
    return floor


def find_floor_part_2(sequence: str) -> int:
    floor = 0
    for i, ch in enumerate(sequence, start=1):
        if ch == "(":
            floor += 1
        elif ch == ")":
            floor -= 1
        if floor == -1:
            return i
    return -1


def run_tests():
    assert find_floor_part_1("(())") == 0
    assert find_floor_part_1("()()") == 0
    assert find_floor_part_1("(((") == 3
    assert find_floor_part_1("(()(()(") == 3
    assert find_floor_part_1("))(((((") == 3
    assert find_floor_part_1("())") == -1
    assert find_floor_part_1("))(") == -1
    assert find_floor_part_1(")))") == -3
    assert find_floor_part_1(")())())") == -3


if __name__ == "__main__":
    run_tests()
    query = read_input("input/day_01.txt")
    print(find_floor_part_1(query))
    print(find_floor_part_2(query))
