from typing import List

def read_input(path: str) -> str:
    with open(path, "r") as f:
        return f.read().strip()

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        return [line.rstrip("\n") for line in f]
