from utils.io import read_input


def track_coordinates(input):
    coordinates = {(0, 0)}
    x = y = 0
    for i in input:
        if i == ">":
            x += 1
        elif i == "<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        else:
            continue
        coordinates.add((x, y))
    return coordinates

def track_santa(input):
    return len(track_coordinates(input))

def track_santa_and_robot(input):
    santa = input[::2]
    robot = input[1::2]
    return len(track_coordinates(santa) | track_coordinates(robot))


def run_tests():
    assert track_santa(">") == 2
    assert track_santa("^>v<") == 4
    assert track_santa("^v^v^v^v^v") == 2

    assert track_santa_and_robot("^v") == 3
    assert track_santa_and_robot("^>v<") == 3
    assert track_santa_and_robot("^v^v^v^v^v") == 11


if __name__ == "__main__":
    run_tests()
    print(track_santa(read_input("input/day_03.txt")))
    print(track_santa_and_robot(read_input("input/day_03.txt")))
