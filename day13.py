from re import findall
from typing import List

import numpy as np


def solve(numbers: List[int], modifier=0) -> int:
    result = 0
    for ax, ay, bx, by, tx, ty in numbers:
        coefficient = np.array([[ax, bx], [ay, by]])
        ordinate = np.array([tx + modifier, ty + modifier])
        a, b = np.round(np.linalg.solve(coefficient, ordinate))
        if a * ax + b * bx == tx + modifier and a * ay + b * by == ty + modifier:
            result += (a * 3) + b
    return int(result)


print("---- Day 13 ----")
with open("input/day13.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    pat = r"\d+"
    data = [[*map(int, findall(pat, line))] for line in file.read().split("\n\n")]
    p1 = solve(data)
    p2 = solve(data, modifier=10**13)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
