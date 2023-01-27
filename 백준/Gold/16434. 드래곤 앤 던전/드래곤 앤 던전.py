"""

"""

import sys
from math import ceil

f = sys.stdin.readline


n, atk = map(int, f().split())

hp = 0
min_hp = 0
for i in range(n):
    t, a, h = map(int, f().split())

    if t == 1:
        hp -= ceil(h / atk - 1) * a
    else:
        atk += a
        hp = 0 if hp + h >= 0 else hp + h
    min_hp = min(min_hp, hp)


print(-min_hp + 1)
