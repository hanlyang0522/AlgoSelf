"""
투포인터의 idx를 언제 옮겨야 하는지 확인할것
"""

import sys

f = sys.stdin.readline


def maxTmp(k, li):
    total = sum(li[:k])
    ans = total

    l, r = 0, k
    while r < len(li):
        total = total + li[r] - li[l]
        r += 1
        l += 1

        ans = max(ans, total)

    return ans


if __name__ == "__main__":
    n, k = map(int, f().split())
    tLi = list(map(int, f().split()))

    print(maxTmp(k, tLi))
