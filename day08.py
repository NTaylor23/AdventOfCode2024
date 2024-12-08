from itertools import combinations
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Tuple


def is_in_range(point: Tuple, lim: int):
    y, x = point
    return y in range(lim) and x in range(lim)


def get_antinodes(p1: Tuple, p2: Tuple, lim: int, repeat=False):
    result = set()
    y1, x1, y2, x2 = *p1, *p2
    y_diff, x_diff = y1 - y2, x1 - x2
    for _ in range(lim - abs(x_diff) + abs(y_diff)):
        y1, x1 = (y1 + y_diff, x1 + x_diff)
        y2, x2 = (y2 - y_diff, x2 - x_diff)
        result |= {*filter(lambda p: is_in_range(p, lim), [(y1, x1), (y2, x2)])}
        if not repeat:
            break
    return result


print("---- Day 08 ----")
with open("input/day08.txt", encoding="utf-8", mode="r") as file:
    data = [line.strip() for line in file.readlines()]
    antennae = {symbol: [] for symbol in [*ascii_uppercase, *ascii_lowercase, *digits]}
    antinode_pairs, antinode_lines = set(), set()

    for i, row in enumerate([list(line) for line in data]):
        for j, col in enumerate(row):
            if col in antennae:
                antennae[col].append((i, j))

    for combination in [combinations(obj, 2) for obj in antennae.values()]:
        for points in combination:
            antinode_pairs |= get_antinodes(*points, len(data))
            antinode_lines |= get_antinodes(*points, len(data), True) | {*points}

    print(f"\tPart 1: {len(antinode_pairs)}")
    print(f"\tPart 2: {len(antinode_lines)}")
