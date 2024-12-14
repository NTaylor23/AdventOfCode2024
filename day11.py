from math import floor, log

cache = {}


def compute(n: int, steps_remaining: int, count: int, ceiling: int) -> int:
    k = (n, ceiling - steps_remaining)
    if k in cache:
        return cache[k]
    if steps_remaining == 0:
        return 1
    if n == 0:
        cache[k] = compute(1, steps_remaining - 1, count, ceiling)
        return cache[k]
    if floor(log(n, 10) + 1) % 2 == 0:
        s = str(n)
        sz = len(s)
        a, b = int(s[0 : (sz // 2)]), int(s[sz // 2 :])
        cache[k] = compute(a, steps_remaining - 1, count, ceiling) + compute(
            b, steps_remaining - 1, count + 1, ceiling
        )
        return cache[k]
    cache[k] = compute(n * 2024, steps_remaining - 1, count, ceiling)
    return cache[k]


print("---- Day 11 ----")
with open("input/day11.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    data = file.readline().split()
    for d in data:
        p1 += compute(int(d), 25, 1, 25)
        cache.clear()

    for d in data:
        p2 += compute(int(d), 75, 1, 75)

    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
