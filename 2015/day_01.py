query = open('input/day_01.txt', 'r').read()
lines = query.split('\n')

def find_floor(sequence: list) -> int:
    result = 0
    for line in sequence:
        for ch in line:
            if ch == "(":
                result +=1
            elif ch == ")":
                result -=1
    return result


assert find_floor(["(())"]) == 0
assert find_floor("()()") == 0
assert find_floor("(((") == 3
assert find_floor("(()(()(") == 3
assert find_floor("))(((((") == 3
assert find_floor("())") == -1
assert find_floor("))(") == -1
assert find_floor(")))") == -3
assert find_floor(")())())") == -3

print(find_floor(lines))