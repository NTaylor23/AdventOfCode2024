from math import log
from operator import add, mul
from typing import Callable, List


def binary_index(i: int) -> int:
    return int(log(i + 1, 2)) + 1


def ternary_index(i: int) -> int:
    return int(log(2 * (i + 1), 3)) + 1


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def use_tree(
    nodes: int,
    k: int,
    target: int,
    numbers: List[int],
    fns: List[Callable],
    idx_fn: Callable,
) -> int:
    tree = [numbers[0] for _ in range(nodes)]
    for i in range(len(tree) // k):
        tree_idx = k * i + 1
        numbers_idx = idx_fn(i)
        if numbers_idx >= len(numbers):
            break
        left = tree[i]  # parent node
        right = numbers[numbers_idx]
        for j in range(k):
            tree[tree_idx + j] = fns[j](left, right)
            if numbers_idx == len(numbers) - 1 and tree[tree_idx + j] == target:
                return target
    return 0


print("---- Day 07 ----")
with open("input/day07.txt", encoding="utf-8", mode="r") as file:
    p1, p2 = 0, 0
    data = file.readlines()
    for line in data:
        values = [*map(int, line.replace(":", "").strip().split())]
        sz = len(values) - 1
        fns = [add, mul]
        binary_tree_result = use_tree(
            nodes=(2 ** (sz + 1)) - 1,
            k=2,
            target=values[0],
            numbers=values[1:],
            fns=[add, mul],
            idx_fn=binary_index,
        )
        p1 += binary_tree_result
        p2 += binary_tree_result
        if not binary_tree_result:
            p2 += use_tree(
                nodes=(3 ** (sz + 1) - 1) // 2,
                k=3,
                target=values[0],
                numbers=values[1:],
                fns=[add, concat, mul],
                idx_fn=ternary_index,
            )
    print(f"\tPart 1: {p1}")
    print(f"\tPart 2: {p2}")
