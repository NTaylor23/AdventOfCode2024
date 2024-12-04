from re import findall

print("---- Day 01 ----")
with open(file="input/day01.txt", encoding="utf-8", mode="r") as file:
    data = [*map(int, findall(r"\d+", file.read()))]
    l, r = data[0::2], data[1::2]
    print(f"\tPart 1: {sum(abs(a - b) for a, b in zip(sorted(l), sorted(r)))}")
    print(f"\tPart 2: {sum(r.count(a) * a for a in l)}")
