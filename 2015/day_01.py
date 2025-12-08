with open('input/day_01.txt', 'r') as f:
    query = f.read().strip()


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


assert find_floor_part_1("(())") == 0
assert find_floor_part_1("()()") == 0
assert find_floor_part_1("(((") == 3
assert find_floor_part_1("(()(()(") == 3
assert find_floor_part_1("))(((((") == 3
assert find_floor_part_1("())") == -1
assert find_floor_part_1("))(") == -1
assert find_floor_part_1(")))") == -3
assert find_floor_part_1(")())())") == -3

print(find_floor_part_1(query))
print(find_floor_part_2(query))
