from collections import defaultdict
from typing import List

from networkx import DiGraph, topological_sort


def median_after_sort(pairs: List[List[str]], update: List[str]) -> int:
    # search ordering rules for defintions relevant to this specific update
    ordering_pairs = filter(lambda p: len({*p} & {*update}) == 2, pairs)

    # topological sort the ordering pairs and sort the update according to that
    tsort = {n: i for i, n in enumerate(topological_sort(DiGraph(ordering_pairs)))}
    update = sorted(update, key=lambda n: tsort[n])

    # median
    return int(update[len(update) // 2])


print("---- Day 05 ----")
with open("input/day05.txt", encoding="utf-8", mode="r") as file:
    from time import perf_counter
    p1, p2 = 0, 0
    start = perf_counter()
    data = file.read().split("\n\n")
    mp = defaultdict(set)
    pairs = [page.split("|") for page in data[0].split("\n")]
    for a, b in pairs:
        mp[a].add(b)

    for line in data[1].split("\n"):
        update = line.strip().split(",")
        previous_pages = {update[0]}
        flag = True
        for i, n in enumerate(update[1:], start=1):
            must_be_before_n = mp[n]
            if previous_pages & must_be_before_n:
                # ordering rules violated. skip for part 1, sort for part 2
                p2 += median_after_sort(pairs, update)
                flag = False
                break
            previous_pages.add(n)
        if flag:
            p1 += int(update[len(update) // 2])
    print(perf_counter() - start)
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
