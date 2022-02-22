import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
input_lines_2 = """8 5
1 5 4 3 2 4 5 2
"""

input_lines_iter = {0: iter(input_lines_1.split("\n")), 2: iter(input_lines_2.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def goldcave(n, m, graph):
    max_gold = -1

    for x in range(1, m):
        for y in range(1, n + 1):
            tmp = max(graph[y - 1][x - 1], graph[y][x - 1], graph[y + 1][x - 1])
            graph[y][x] += tmp

    print(graph)

    for y in range(1, n + 1):
        max_gold = max(max_gold, graph[y][-1])

    return max_gold


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        li = list(map(int, input().split()))
        graph = [[0 for i in range(m)]]
        for i in range(n):
            graph.append(li[i * m : (i + 1) * m])
        graph.append([0 for i in range(m)])
        print(graph)
        print(goldcave(n, m, graph))
