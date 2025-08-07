import argparse
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """5
3 2 1 1 9
"""  # 8
input_lines_2 = """8
1 5 4 3 2 4 5 2
"""  # 27

input_lines_iter = {0: iter(input_lines_2.split("\n")), 2: iter(input_lines_2.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def cannot(N, coins):
    cost = set([])

    for i in range(1, len(coins) + 1):
        for comb in combinations(coins, i):
            cost.add(sum(comb))
    print(cost)
    cost = list(cost)

    for i in range(len(cost) - 1):
        if cost[i + 1] - cost[i] != 1:
            return cost[i] + 1

    return cost[-1] + 1


if __name__ == "__main__":
    N = int(input())
    coins = list(map(int, input().split()))

    print(cannot(N, coins))
