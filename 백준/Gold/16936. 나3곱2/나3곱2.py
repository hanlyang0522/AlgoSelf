"""
1. 임의의 수 기준으로 앞/뒤 비교해서 nums에서 하나씩 빼서 붙이기 --> 시간초과
2. 소인수분해 후 정렬, 3은 줄어들고, 2는 증가하는 순서로
"""

import sys

f = sys.stdin.readline


def d3m2(n, nums):
    li = []
    for num in nums:
        c2, c3 = 0, 0
        tmp = num
        while num % 2 == 0:
            num = num//2
            c2 += 1
        while num % 3 == 0:
            num = num//3
            c3 += 1

        li.append([tmp, c2, c3])
    li = sorted(li, key=lambda x: (x[1], -x[2]))

    for i in range(n):
        print(li[i][0], end=" ")


if __name__ == "__main__":
    n = int(f())
    nums = list(map(int, f().split()))
    d3m2(n, nums)
