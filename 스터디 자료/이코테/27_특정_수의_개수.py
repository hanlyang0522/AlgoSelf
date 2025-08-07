# 1. 이진탐색 2번?


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """7 2
1 1 2 2 2 2 3
"""  # 4
input_lines_2 = """7 4
1 1 2 2 2 2 3
"""  # -1
input_lines_3 = """7 1
1 1 2 2 2 2 3"""  # 2
input_lines_4 = """7 0
1 1 2 2 2 2 3"""  # -1
input_lines_5 = """7 3
1 1 2 2 2 2 3"""  # 1
input_lines_iter = {0: iter(input_lines_1.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def countNum(N, x, li):
    l, r = 0, N - 1

    while l <= r:
        m = (l + r) // 2

        if li[m] < x:
            l = m + 1
        elif li[m] > x:
            r = m - 1
        elif li[m] == x and li[m - 1] == x:
            r = m - 1
    print(m)

    return -1


if __name__ == "__main__":
    N, x = map(int, input().split())
    li = list(map(int, input().split()))
