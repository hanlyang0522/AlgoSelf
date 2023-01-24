"""
1. DFS로 풀어야되나? 기본은 알파벳마다 1개씩 할당 후 계산하는 방향으로
2. 최대 9! = 3.6*10^5라 완탐 가능
3. 순열로 풀었더니 시간초과
-> 알파벳이 10개를 넘을 경우를 고려안함
"""

import sys
from itertools import permutations
from collections import defaultdict

f = sys.stdin.readline


nums = list(f().split())

letterPool = []
leftDi = defaultdict(int)
rightDi = defaultdict(int)

for i in range(len(nums)):
    cnt = 10 ** (len(nums[i]) - 1)
    for letter in nums[i]:
        if letter not in letterPool:
            letterPool.append(letter)
        if i != 2:
            leftDi[letter] += cnt
        else:
            rightDi[letter] += cnt
        cnt /= 10

# print(leftDi, rightDi)


for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], len(letterPool)):
    if len(letterPool)>10:
        break
    di = {k: v for k, v in zip(letterPool, perm)}
    # print(di)

    l, r = 0, 0
    for k, v in leftDi.items():
        l += di[k] * v
    for k, v in rightDi.items():
        r += di[k] * v

    if l == r:
        print("YES")
        exit(0)
    # break


print("NO")
