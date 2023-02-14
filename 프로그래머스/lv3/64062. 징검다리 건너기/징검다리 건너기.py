'''
1. k만큼 나눈 구간의 최댓값 중 최솟값 구하기
--> 해당 구간에서 모든 돌이 0이 될 때까지는 `구간 중 최댓값`만큼 지나가야함
2. val,idx 순으로 pq에 저장, 이후 매 iter마다 pq의 최댓값의 idx가 범위에 해당하지 않을 경우에만 pop
'''

from heapq import heappush, heappop

def solution(stones, k):
    pq = [] # val,idx 순서로 저장
    for i in range(k):
        heappush(pq, [-stones[i], i]) # 최대힙이라 부호 바꿔서 push

    ans = -pq[0][0]
    i+=1

    while i < len(stones): # O(N)
        heappush(pq, [-stones[i], i]) # 최대 N번만 꺼낼 수 있어서 O(NlogN)
        i+=1 

        while pq[0][1] < i-k: # 최댓값이 범위에 해당하지 않는 경우는 pop
            heappop(pq) # 최대 N번만 꺼낼 수 있어서 O(NlogN)

        ans = min(ans, -pq[0][0])

    return ans