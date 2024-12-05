def rotate_90_deg(s: str) -> str:
    arr = [list(row) for row in s.split("\n")]
    return "\n".join(["".join([arr[i][j] for i in range(rows)]) for j in range(cols)])


def count(s: str) -> int:
    return s.count("XMAS") + s.count("SAMX")


def count_xmas_occurences(grid, row, col) -> int:
    first = "".join(grid[row + i][col + i] for i in range(4))
    second = "".join(grid[row + 4 - i - 1][col + i] for i in range(4))
    choices = ["XMAS", "SAMX"]
    return int(first in choices) + int(second in choices)


def count_mas_occurences(grid, row, col):
    first = "".join(grid[row + i][col + i] for i in range(3))
    second = "".join(grid[row + 3 - i - 1][col + i] for i in range(3))
    choices = ["SAM", "MAS"]
    return int(first in choices and second in choices)


print("---- Day 04 ----")
with open("input/day04.txt", encoding="utf-8", mode="r") as file:
    word_search = file.read()
    word_search_rotated = rotate_90_deg(word_search)
    arr = [list(line.strip()) for line in word_search.split("\n")]

    p1, p2 = 0, 0
    p1 += count(word_search) + count(word_search_rotated)

    rows, cols = len(arr), len(arr[0])
    for r in range(rows - 3):
        for c in range(cols - 3):
            p1 += count_xmas_occurences(arr, r, c)

    for r in range(rows - 2):
        for c in range(cols - 2):
            p2 += count_mas_occurences(arr, r, c)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
