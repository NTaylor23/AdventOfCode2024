from heapq import heappop, heappush
from typing import Set, Tuple


def find_paths(
    grid: Set[Tuple[int, int]], start: Tuple[int, int], end: Tuple[int, int]
) -> int:
    seen, paths = {}, []
    stack = [(0, 0, *start, [start])]  # cost, direction, y, x, [path]
    while stack:
        score, d_i, y, x, path = heappop(stack)

        if seen.get((y, x, d_i), float("inf")) < score:
            continue

        if (y, x) == end:
            paths.append((score, path))
            continue

        seen[(y, x, d_i)] = score

        for i, (dy, dx) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            if (y + dy, x + dx) not in grid:
                continue
            current_score = 1001 if i != d_i else 1
            current_path = path + [(y + dy, x + dx)]
            heappush(stack, (score + current_score, i, y + dy, x + dx, current_path))
    return paths


print("---- Day 16 ----")
with open("input/day16.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    start: Tuple[int, int]
    end: Tuple[int, int]
    nodes = set()
    for y, row in enumerate(file.readlines()):
        for x, col in enumerate(row):
            if col == "#":
                continue
            if col == "S":
                start = (y, x)
            elif col == "E":
                end = (y, x)
            nodes.add((y, x))

    valid_paths = find_paths(nodes, start, end)
    best_path_score = min(valid_paths, key=lambda t: t[0])[0]
    points_visited = set()

    for path in filter(lambda p: p[0] == best_path_score, valid_paths):
        path = path[1]
        for point in path:
            points_visited.add(point)

    p1 = best_path_score
    p2 = len(points_visited)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
