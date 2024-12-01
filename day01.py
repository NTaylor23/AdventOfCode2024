from re import findall
from collections import Counter

print("---- Day 01 ----")


with open(file="input/day01.txt", mode="r", encoding="utf-8") as file:
    data = [findall(r"\d+", line) for line in file.readlines()]
    left = [int(pair[0]) for pair in data]
    right = [int(pair[-1]) for pair in data]
    counter = Counter(right)
    p1 = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
    p2 = sum(counter.get(a, 0) * a for a in left)
    print(f"\tPart 1: {p1}\n\tPart 2: {p2}")
