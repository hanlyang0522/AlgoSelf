import sys
from heapq import heappush, heappop

f = sys.stdin.readline


def picnic(K, N, F):
    if K == 1:
        print(1)
        return

    li = [[] for _ in range(N + 1)]  # 친구 목록

    for _ in range(F):
        a, b = map(int, f().split())
        li[a].append(b)
        li[b].append(a)

    for i in range(1, N + 1):
        li[i].sort()

    for start in range(1, N + 1):
        rst = bfs(start, li, K, N)
        if rst:
            rst.sort()
            for num in rst:
                print(num)
            return
    print(-1)


def bfs(start, li, K, N):
    visit = [False] * (N + 1)
    path = [start]
    pq = [start]
    visit[start] = True

    while pq:
        now = heappop(pq)

        for nxt in li[now]:
            if not visit[nxt]:
                visit[nxt] = True
                flag = False

                # 현재까지 친구와 친구인지 검사
                for target in path:
                    if nxt not in li[target]:
                        flag = True
                        break

                if not flag:
                    path.append(nxt)
                    if len(path) == K:
                        return path
                    heappush(pq, nxt)


if __name__ == "__main__":

    K, N, F = map(int, f().split())

    picnic(K, N, F)
