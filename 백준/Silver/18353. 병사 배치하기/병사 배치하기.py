# 오름차순으로 정렬
# bisect로 idx 찾은 후 맨 뒤라면 추가
# 전체 - 정렬 후 길이
from bisect import bisect, bisect_left
import sys

f = sys.stdin.readline


def maxFp(sldrs):
    lis = [sldrs[0]]

    for sld in sldrs[1:]:
        # sld가 들어갈 위치 찾음, 같은 값이라면 왼쪽으로 들어감
        idx = bisect_left(lis, sld)  

        if idx >= len(lis):
            lis.append(sld)
        else:
            # idx보다 작은 값이 idx에 insert 돼야 정렬을 만족하기 때문에 
            # idx를 sld로 대체한다면 더 작은 값으로 대체됨
            lis[idx] = sld

    return len(sldrs) - len(lis)


if __name__ == "__main__":
    n = int(f())
    sldrs = list(map(int, f().split()))
    sldrs.reverse()

    print(maxFp(sldrs))
