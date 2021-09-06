import sys
import heapq

f = sys.stdin.readline
li = []
N = int(f())

for num in map(int, f().split()):
    heapq.heappush(li, num)

for i in range(1, N):
    tmp = list(map(int, f().split()))

    for j in range(N):
        if tmp[j] > li[0]:
            # heap의 최솟값보다 클 경우 push하고 최솟값은 pop
            heapq.heappush(li, tmp[j])
            heapq.heappop(li)

# why??
print(li[0])


# def get_max_col(N, li):
#     max_col = 0
#     max_val = -(sys.maxsize)

#     for i in range(N):
#         if li[i][-1] > max_val:
#             max_val = li[i][-1]
#             max_col = i

#     return max_col

# N = int(sys.stdin.readline())
# li = [[] for _ in range(N)]

# for i in range(N):
#     li[i] = list(map(int, sys.stdin.readline().split()))

# for i in range(N-1):
#     li[get_max_col(N, li)].pop()

# print(li[get_max_col(N, li)][-1])