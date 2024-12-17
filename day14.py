from re import findall
from typing import List, Tuple

ROWS, COLS = 103, 101


def get_position(px: int, py: int, vx: int, vy: int) -> Tuple[int, int]:
    px = (px + vx) % COLS
    py = (py + vy) % ROWS
    return (px, py)


def count_robots_in_quadrants(grid: List[List[int]]) -> int:
    safety_factors = [0, 0, 0, 0]
    mid_y, mid_x = ROWS // 2, COLS // 2
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if not col or y == mid_y or x == mid_x:
                continue
            if y < mid_y and x < mid_x:
                safety_factors[0] += col
            elif y < mid_y and x > mid_x:
                safety_factors[1] += col
            elif y > mid_y and x < mid_x:
                safety_factors[2] += col
            else:
                safety_factors[3] += col
    return safety_factors[0] * safety_factors[1] * safety_factors[2] * safety_factors[3]


def find_tree(grid: List[List[int]]) -> bool:
    for row in grid:
        r = "".join(["#" if n > 0 else "." for n in row])
        if "###############################" in r:
            return True
    return False


def process(instructions) -> Tuple[int, int]:
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    positions = []
    p1, p2 = 0, 0
    for line in instructions:
        px, py, vx, vy = map(int, findall(r"-?\d+", line.strip()))
        grid[py][px] = 1
        positions.append([px, py, vx, vy])

    for iteration in range(1, 10000):  # arbitrary limit ¯\_(ツ)_/¯
        for i in range(len(instructions)):
            px, py, vx, vy = positions[i]
            grid[py][px] = max(0, grid[py][px] - 1)
            x, y = get_position(px, py, vx, vy)
            grid[y][x] += 1
            positions[i][0], positions[i][1] = x, y
        if iteration == 100:
            p1 = count_robots_in_quadrants(grid)
        if find_tree(grid):
            p2 = iteration
            return p1, p2
        iteration += 1
    return 0, 0


print("---- Day 14 ----")
with open("input/day14.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = process(file.readlines())
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
