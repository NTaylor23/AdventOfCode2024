from collections import deque
from typing import Dict, Tuple

DIMS = 213


def bfs(mp: Dict[Tuple[int, int], int]) -> int:
    stack = deque([(0, 0, 0)])
    seen = set()
    shortest_path_cost = float("inf")
    while stack:
        score, y, x = stack.popleft()
        if (y, x) in seen:
            continue
        if (y, x) == (DIMS, DIMS):
            shortest_path_cost = min(score, shortest_path_cost)
            continue
        seen.add((y, x))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (y + dy, x + dx) in mp and not mp[(y + dy, x + dx)]:
                stack.append((score + 1, y + dy, x + dx))
    return shortest_path_cost


print("---- Day 18 ----")
with open("input/day18.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, ""
    mp = {(i, j): 0 for j in range(DIMS + 1) for i in range(DIMS + 1)}
    byte_locations = [[*map(int, pair.split(","))] for pair in file.readlines()]

    # set all bytes in list
    for bx, by in byte_locations:
        mp[(by, bx)] = 1

    # work down the list of bytes backwards until a config with a path is found
    last_processed_byte = "0,0"
    while bfs(mp) == float("inf"):
        lx, ly = byte_locations.pop()
        mp[(ly, lx)] = 0
        last_processed_byte = f"{lx},{ly}"

    p2 = last_processed_byte

    # for part 1, we only want to process the map with the first 1024 bytes added
    while len(byte_locations) > 1024:
        lx, ly = byte_locations.pop()
        mp[(ly, lx)] = 0

    p1 = bfs(mp)
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
