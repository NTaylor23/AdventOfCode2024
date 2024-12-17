from collections import defaultdict, deque
from typing import DefaultDict, Set, Tuple

ROBOT = "@"
BOX = "O"
WALL = "#"
BLANK = "."
BOX_L = "["
BOX_R = "]"

DELTAS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def move_p1(mp: DefaultDict[str, Set[Tuple[int, int]]], pos: Tuple[int, int], dir: str):
    y, x, dy, dx = *pos, *DELTAS[dir]
    new_pos = (y + dy, x + dx)
    boxes_to_move = []
    if new_pos in mp[BOX]:
        yy, xx = new_pos
        while (yy, xx) in mp[BOX]:
            boxes_to_move.append((yy, xx))
            yy, xx = yy + dy, xx + dx
        ly, lx = boxes_to_move[-1]
        if (ly + dy, lx + dx) in mp[WALL]:
            return pos
        for box_pos in boxes_to_move:
            by, bx = box_pos
            mp[BOX].add((by + dy, bx + dx))
        mp[BOX].discard(new_pos)
    elif new_pos in mp[WALL]:
        return pos

    return new_pos


def debug_print(mp, rows, cols, py, px):
    g = [["." for _ in range(cols)] for _ in range(rows)]
    for k, v in mp.items():
        for y, x in v:
            g[y][x] = k
    g[py][px] = "@"
    print(py, px)
    for row in g:
        print("".join(row))
    print()


print("---- Day 15 ----")
with open("input/day15.txt", encoding="utf-8", mode="r") as file:
    grid, movements = file.read().split("\n\n")
    grid = grid.split("\n")  # get rid of this when finished

    rows, cols = len(grid), len(grid[0])
    original, scaled = defaultdict(set), defaultdict(set)

    for y, row in enumerate(grid):
        doubled_row = "".join([c * 2 for c in row]).replace("OO", "[]")

        for x, col in enumerate(row):
            original[col].add((y, x))

        for x, col in enumerate(doubled_row):
            if x and doubled_row[x - 1] == ROBOT:
                continue
            scaled[col].add((y, x))

    y, x = original[ROBOT].pop()
    cy, cx = scaled[ROBOT].pop()
    for dir in movements.replace("\n", ""):
        y, x = move_p1(original, (y, x), dir)
        cy, cx = move_p1(scaled, (cy, cx), dir)
        # debug_print(scaled, rows, cols * 2, cy, cx)

    p1 = sum(map(lambda pos: 100 * pos[0] + pos[1], original[BOX]))
    # p2 = sum(map(lambda pos: 100 * pos[0] + pos[1], scaled[BOX]))
    p2 = 0
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
