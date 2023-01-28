"""
n = 10, 길이 = 8이라 완탐 가능
매 입력마다 자리수에 알파벳 넣고 상위 자리수에 있을 경우 갱신
--> 단순히 제일 앞에 나오는거 말고 해당 알파벳이 총 몇번 나왔는지를 계산!!
"""

import sys
from collections import defaultdict

f = sys.stdin.readline


n = int(f())
di = defaultdict(int)

for i in range(n):
    num = f()[:-1]

    tmp = 10 ** (len(num) - 1)
    for i in range(len(num)):
        di[num[i]] += tmp
        tmp /= 10

di = sorted(di.items(), key=lambda x: x[1], reverse=True)


cnt = 9
ans = 0
for _, v in di:
    ans += cnt * v
    cnt -= 1


print(int(ans))
