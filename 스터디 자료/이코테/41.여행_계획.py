import argparse
from collections import deque
from tabnanny import check

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""  # YES

input_lines_2 = """5 4
0 1 0 0 0
1 0 1 0 0
0 1 0 0 0
0 0 0 0 1
0 0 0 1 0
2 3 4 3
"""  # NO

input_lines_3 = """5 4
0 1 0 1 0
1 0 0 1 0
0 0 0 0 1
1 1 0 0 0
0 0 1 0 0
2 1 4 1 5
"""  # NO

input_lines_4 = """8 6
0 1 0 0 0 1 1 0
1 0 1 0 0 0 0 1
0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0
1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
0 1 0 0 0 0 1 0
1 3 2 6 7 8 
"""  # YES

input_lines_5 = """8 7
0 1 0 0 0 1 1 0
1 0 1 0 0 0 0 1
0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0
1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
0 1 0 0 0 0 1 0
1 3 2 6 7 8 4
"""  # NO

input_lines_6 = """8 2
0 1 0 0 0 1 1 0
1 0 1 0 0 0 0 1
0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0
1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
0 1 0 0 0 0 1 0
4 5
"""  # YES

input_lines_iter = {0: iter(input_lines_4.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


# parent = []


def get_parent(v):
    if parent[v] == v:
        return v
    else:
        return get_parent(parent[v])


def make_union(v1, v2):
    a = get_parent(v1)
    b = get_parent(v2)
    if a < b:
        parent[v2] = a
    else:
        parent[v1] = b


def check_union(v1, v2):
    a = get_parent(v1)
    b = get_parent(v2)
    if a != b:
        return 1
    else:
        return 0


def tour_check(N, M, graph, tours):
    # parent.extend([i for i in range(N)])
    global parent
    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i, N):
            if graph[i][j] == 1 and check_union(i, j):
                make_union(i, j)

    tmp_par = parent[tours[0]]
    for tour in tours:
        if parent[tour - 1] != tmp_par:
            print("NO")
            return 0
    print("YES")


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    tours = list(map(int, input().split()))
    print(graph, tours)

    tour_check(N, M, graph, tours)
