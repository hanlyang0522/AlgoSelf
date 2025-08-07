import argparse
import heapq

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1 
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""

input_lines_iter = {0: iter(input_lines_1.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dijkstra(n, li):
    q = []
    heapq.heappush(q, (li[0][0], (0, 0)))  # fuel, 좌표
    dp = [[1e9 for _ in range(n)] for __ in range(n)]  # 방문에 따라 갱신
    dp[0][0] = li[0][0]

    while q:
        dist, (y, x) = heapq.heappop(q)
        # if dp[y][x] < dist:  # 이미 최단거리라 방문할 필요 x
        #     continue

        for dy, dx in dirs:
            ty, tx = y + dy, x + dx

            if ty in range(n) and tx in range(n):  # 그래프를 내에 있을 경우
                cost = dist + li[ty][tx]
                if cost < dp[ty][tx]:
                    dp[ty][tx] = cost
                    heapq.heappush(q, (cost, (ty, tx)))

    print(dp)
    return dp[n - 1][n - 1]


if __name__ == "__main__":
    TC = int(input())

    for t in range(TC):
        n = int(input())
        li = []
        for i in range(n):
            li.append(list(map(int, input().split())))

        print(dijkstra(n, li))
