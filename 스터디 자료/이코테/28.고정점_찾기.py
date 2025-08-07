import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """5
-16 -6 1 3 7
"""  # 3
input_lines_2 = """7
-15 -4 2 8 9 13 15
"""  # 2
input_lines_3 = """7
-15 -4 3 8 9 13 15
"""  # -1
input_lines_4 = """7
0 2 3 8 9 13 15
"""  # 0
input_lines_5 = """7
-1 1 3 8 9 13 15
"""  # 1
input_lines_6 = """8
-15 -4 -3 0 1 2 3 7
"""  # 7
input_lines_iter = {0: iter(input_lines_6.split("\n"))}


def input():
    return next(input_lines_iter[args.test])


# 이후 python .py --test 1 2 3 처럼 사용


def find_fix(N, li):
    l, r = 0, len(li) - 1
    if li[l] == l:
        print(l)
        return 0
    elif li[r] == r:
        print(r)
        return 0

    while l <= r:
        m = (l + r) // 2
        if li[m] < m:
            l = m + 1
        elif li[m] > m:
            r = m - 1
        else:
            print(m)
            return 0

    print(-1)


if __name__ == "__main__":
    N = int(input())
    li = list(map(int, input().split()))

    find_fix(N, li)
