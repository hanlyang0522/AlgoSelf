import sys
from collections import defaultdict

N = int(sys.stdin.readline())
N_pool = list(map(int, sys.stdin.readline().split()))
N_list = defaultdict()
for n in N_pool:
    N_list[n] = 1

M = int(sys.stdin.readline())
M_pool = list(map(int, sys.stdin.readline().split()))


for m in M_pool:
    if m in N_list:
        print('1', end=' ')
    else:
        print('0', end=' ')


# N_pool.sort()
# M_pool.sort()
# print(N_pool)
# print(M_pool)

# n_idx = 0
# m_idx = 0

# while m_idx < len(M_pool):
#     if n_idx == len(N_pool)-1:
#         print('0', end=' ')
#         m_idx = m_idx + 1
        
#     elif M_pool[m_idx] < N_pool[n_idx]:
#         print('0', end=' ')
#         m_idx = m_idx + 1

#     elif M_pool[m_idx] == N_pool[n_idx]:
#         print('1', end=' ')
#         n_idx = n_idx + 1
#         m_idx = m_idx + 1
        
#     elif M_pool[m_idx] > N_pool[n_idx]:
#         print('0', end=' ')
#         n_idx = n_idx + 1
#         m_idx = m_idx + 1
