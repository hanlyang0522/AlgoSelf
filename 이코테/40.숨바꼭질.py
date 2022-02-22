import argparse
from math import dist
import sys
import heapq

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""

input_lines_iter = {0: iter(input_lines_1.split("\n")), 2: iter(input_lines_2.split("\n"))}


def input():
    return next(input_lines_iter[args.test])


# 이후 python .py --test 1 2 3 처럼 사용
def far_town(N, M, graph):
    distances = [sys.maxsize for i in range(N)]
    distances[0] = 0
    queue = []
    heapq.heappush(queue, (distances[0], 0))

    while queue:
        current_dist, node = heapq.heappop(queue)
        if distances[node] < current_dist:
            continue

        for adj_node in graph[node]:
            weighted_dist = current_dist + 1

            if weighted_dist < distances[adj_node]:
                distances[adj_node] = weighted_dist
                heapq.heappush(queue, (weighted_dist, adj_node))

    dic = {}
    for i in range(N):
        dic[i + 1] = distances[i]
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    print(dic)

    flag = True
    cnt = 0
    for k, v in dic.items():
        if flag:
            far_town, far_dist = k, v
            flag = False
        if v == far_dist:
            cnt += 1
        else:
            break

    return far_town, far_dist, cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for j in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    # print(graph)

    print(far_town(N, M, graph))
