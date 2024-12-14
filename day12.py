from collections import defaultdict, deque
from typing import List, Set, Tuple

seen = set()


def count_corners(r: Set) -> int:
    if len(r) == 1:
        return 4
    s = 0
    for y, x in r:
        for n in [-1, 1]:
            s += (y + n, x) not in r and (y, x + n) not in r
            s += (y - n, x) not in r and (y, x + n) not in r
            s += (y, x + n) in r and (y + n, x) in r and (y + n, x + n) not in r
            s += (y, x + n) in r and (y - n, x) in r and (y - n, x + n) not in r
    return s


def bfs(
    grid: List[List[int]], plant: str, pos: Tuple[int, int]
) -> List[Tuple[int, int]]:
    sz = len(grid)
    stack = deque([pos])
    region = set()
    perimeter = 0
    while stack:
        y, x = stack.pop()
        if (y, x) in seen:
            continue
        seen.add((y, x))  # global scope
        region.add((y, x))  # block scope
        for dy, dx in [(y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x)]:
            if dy in range(sz) and dx in range(sz) and grid[dy][dx] == plant:
                stack.append((dy, dx))
            else:
                perimeter += 1
    return [*region, (perimeter, count_corners(region))]


print("---- Day 12 ----")
with open("input/day12.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    mp = defaultdict(list)
    data = [[*line.strip()] for line in file.readlines()]
    for y, row in enumerate(data):
        for x, plant_type in enumerate(row):
            plot = bfs(data, plant_type, (y, x))
            if len(plot) > 1:
                mp[plant_type].append(plot)

    for k, plant_type in mp.items():
        for plot in plant_type:
            perimeter, sides = plot.pop()
            area = len(plot)
            p1 += area * perimeter
            p2 += area * sides

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
