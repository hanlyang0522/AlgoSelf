import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""

input_lines_iter = {0: iter(input_lines_1.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def get_parent(parent, r):
    if parent[r] == r:
        return r
    return get_parent(parent, parent[r])


def make_union(parent, r1, r2):
    a = get_parent(parent, r1)
    b = get_parent(parent, r2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def check_parent(parent, r1, r2):
    a = get_parent(parent, r1)
    b = get_parent(parent, r2)
    if a != b:
        return 1
    else:
        return 0


def max_save(N, M, roads):
    roads.sort(key=lambda x: x[2])
    # print(roads)
    parent = [i for i in range(N)]
    save = 0

    for road in roads:
        if check_parent(parent, road[0], road[1]):  # union 아닐 경우
            make_union(parent, road[0], road[1])
        else:
            save += road[2]

    print(parent, save)


if __name__ == "__main__":
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))

    max_save(N, M, roads)
