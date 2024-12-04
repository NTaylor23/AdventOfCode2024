from operator import gt, lt
from typing import List


def is_valid(levels: List[int]) -> bool:
    comparison = lt if levels[0] < levels[1] else gt
    zipped = list(zip(levels, levels[1:]))

    # check constraint for numbers differing by >= 1 and <= 3
    if any(abs(a - b) not in range(1, 4) for a, b in zipped):
        return False

    # check constraint for strictly increasing or decreasing
    return all(comparison(a, b) for a, b in zipped)


def try_delete(levels: List[int]) -> bool:
    # try deleting each level individually until something satisfies `is_valid`
    return any(
        is_valid(d) for d in [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
    )


print("---- Day 02 ----")
with open(file="input/day02.txt", encoding="utf-8", mode="r") as file:
    data = [[*map(int, line.split())] for line in file.readlines()]

    # reuse this to avoid reprocessing valid lists
    check_valid = [is_valid(nums) for nums in data]
    p1 = sum(check_valid)

    for i, nums in enumerate(data):
        if not check_valid[i]:
            check_valid[i] = try_delete(nums)
    p2 = sum(check_valid)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
