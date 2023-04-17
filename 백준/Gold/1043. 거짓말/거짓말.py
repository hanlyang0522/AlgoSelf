"""
union-find아니면 set 사용
"""

import sys

f = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, f().split())
    klist = set(f().split()[1:])
    pts =[]

    for _ in range(m):
        pts.append(set(f().split()[1:]))

    # 모든 파티 확인
    for _ in range(m):
        for party in pts:
            if party & klist: # 교집합이 있을 경우
                klist = klist.union(party)

    cnt = 0
    for party in pts:
        if party & klist:
            continue
        cnt+=1

    print(cnt)