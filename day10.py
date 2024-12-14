from typing import Dict, Tuple


def find_trails(
    mp: Dict[Tuple[int, int], int], pos: Tuple[int, int], count_distinct=False
) -> int:
    result = 0
    seen = set()
    stack = [pos]
    while stack:
        y, x = stack.pop()
        elevation = mp[(y, x)]

        if (y, x) in seen and not count_distinct:
            continue

        seen.add((y, x))
        if mp[(y, x)] == 9:
            result += 1
            continue

        for adjacent_point in [
            (y + i, x + j) for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ]:
            if adjacent_point in mp and mp[adjacent_point] == elevation + 1:
                stack.append(adjacent_point)

    return result


print("---- Day 10 ----")
with open("input/day10.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    mp = {}
    for y, row in enumerate(file.readlines()):
        for x, col in enumerate(row.strip()):
            if col != ".":
                mp[(y, x)] = int(col)

    for pos, elevation in filter(lambda p: p[1] == 0, mp.items()):
        p1 += find_trails(mp=mp, pos=pos)
        p2 += find_trails(mp=mp, pos=pos, count_distinct=True)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
