'''
1. 무적권 있으면 무적권 사용, enemy는 heapq에 저장
2. 무적권 없으면 heapq에서 pull
    (지나간 라운드 중 enemy 적은것부터 소모했다고 가정)
'''

from heapq import heappush, heappop

def solution(n, k, enemy):
    q = []
    rnd = 0
    for en in enemy:
        if k>0: # 무적권 있을 경우
            k-=1
            heappush(q, en)
        else:
            heappush(q, en)
            if q:
                n -= heappop(q)
            else:
                n -= en

            if n<0:
                return rnd

        rnd+=1

    return rnd