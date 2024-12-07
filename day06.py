from multiprocessing import Pool
from typing import Set, Tuple


def traverse(mp: Set, start: Tuple, size: int, new_obstacle: Tuple) -> Set:
    if new_obstacle:
        mp.add(new_obstacle)

    idx = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left
    current_direction = directions[idx]

    visited_obstacles = set()
    visited_positions = {start}

    prev = start

    while True:
        y, x = prev
        y += current_direction[0]
        x += current_direction[1]

        if y not in range(size) or x not in range(size):
            break

        if (y, x) in mp:
            idx = (idx + 1) % 4
            current_direction = directions[idx]

            if (y, x, idx) in visited_obstacles:
                # already met this obstacle once before while moving in the same direction,
                # soooooo we're in a cycle, and will return an empty set
                return {}
            visited_obstacles.add((y, x, idx))
            continue

        prev = (y, x)
        visited_positions.add((y, x))

    return visited_positions


def worker(args):
    return traverse(*args)


if __name__ == "__main__":  # for multiprocessing.Pool()
    print("---- Day 06 ----")
    with open("input/day06.txt", encoding="utf-8", mode="r") as file:
        p1, p2, sy, sx = 0, 0, 0, 0
        data = [line.strip() for line in file.readlines()]
        obstacles = set()

        for y, row in enumerate(data):
            for x, col in enumerate(row):
                if col == "#":
                    obstacles.add((y, x))
                elif col == "^":
                    # this is the start point
                    sy, sx = y, x

        visited_locations_without_cycle = traverse(
            obstacles, start=(sy, sx), size=len(data), new_obstacle=None
        )
        p1 = len(visited_locations_without_cycle)

        with Pool() as process_pool:
            tasks = [
                [{*obstacles}, (sy, sx), len(data), pos]
                for pos in visited_locations_without_cycle
            ]
            results = process_pool.imap_unordered(worker, tasks)
            p2 = sum(len(result) == 0 for result in results)

        print(f"\tPart 1: {p1}")
        print(f"\tPart 2: {p2}")
