import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """5
2 3 1 2 2
"""
input_lines_2 = """6
4 3 3 3 3 2
"""
input_lines_3 = """7
2 2 3 4 2 2 3
"""

input_lines_iter = {0: iter(input_lines_3.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


# '공포도 = 현재 그룹 인원수'일 경우 그룹 완성하고 다음 그룹으로 넘어감
def maxTravel(n, trav):
    trav.sort()
    group, cnt = 0, 1

    for t in trav:
        if cnt >= t:
            group += 1
            cnt = 1
        else:
            cnt += 1

    return group


if __name__ == "__main__":
    N = int(input())
    travelers = list(map(int, input().split()))
    print(maxTravel(N, travelers))
