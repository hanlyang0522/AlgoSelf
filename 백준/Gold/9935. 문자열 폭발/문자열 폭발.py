import sys
from itertools import combinations
from collections import deque

f = sys.stdin.readline


def solve():
    s = input()
    bomb = input()

    len_b = len(bomb)
    last_b = bomb[-1]
    stack = []

    for char in s:
        stack.append(char)

        if char==last_b and len(stack) >= len_b:
            if "".join(stack[-len_b:]) == bomb:
                for _ in range(len_b):
                    stack.pop()

    if not stack:
        print("FRULA")
    else:
        print("".join(stack))

    pass


if __name__ == "__main__":
    solve()
