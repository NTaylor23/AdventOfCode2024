from typing import List


def solve_p1(nums: List[int]) -> int:
    disk = []
    for i, symbol in enumerate(nums):
        if i % 2 == 0:
            disk.extend([i // 2] * symbol)
        else:
            disk.extend([-1] * symbol)

    spaces = [i for i, n in enumerate(disk) if n == -1]
    for i in spaces:
        while disk[-1] < 0:
            disk.pop()
        if len(disk) <= i:
            break
        disk[i] = disk.pop()
    return sum(i * file for i, file in enumerate(disk))


def solve_p2(nums: List[int]) -> int:
    files, spaces = {}, []
    file_id, position, result = 0, 0, 0

    for i, n in enumerate(nums):
        if i % 2 == 0:
            files[file_id] = (position, n)
            file_id += 1
        else:
            spaces.append((position, n))
        position += n

    while file_id:
        file_id -= 1
        position, size = files[file_id]
        for i, (start, length) in enumerate(spaces):
            if start >= position:
                spaces = spaces[:i]
                break
            if size <= length:
                files[file_id] = (start, size)
                if size == length:
                    spaces.pop(i)
                else:
                    spaces[i] = (start + size, length - size)
                break
    for file_id, (idx, length) in files.items():
        for i in range(idx, idx + length):
            result += file_id * i
    return result


print("---- Day 09 ----")
with open("input/day09.txt", encoding="utf-8", mode="r") as file:
    data = list(map(int, file.read()))
    p1, p2 = 0, 0
    p1 = solve_p1(data)
    p2 = solve_p2(data)
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
