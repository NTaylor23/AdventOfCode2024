from re import compile, findall, finditer
from operator import mul

def multiply(operation):
    return mul(*map(int, findall(r"\d+", operation)))


print("---- Day 03 ----")
with open("input/day03.txt", encoding="utf-8", mode="r") as file:
    data = file.read()
    p1, p2, flag = 0, 0, True
    for m in finditer(compile(r"(do(n\'t)?\x28\x29)|(mul\x28\d+,\d+\x29)"), data):
        val = m.group()
        if val == "do()":
            flag = True
        elif val == "don't()":
            flag = False
        else:
            p1 += multiply(val)
            p2 += multiply(val) if flag else 0
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
