import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """1
"""
input_lines_2 = """4
"""

input_lines_iter = {0: iter(input_lines_1.split("\n")), 1: iter(input_lines_2.split("\n"))}


def input():
    return next(input_lines_iter[args.test])


def ugly(n):
    uglys = [1]
    nums = [2, 3, 5]

    while n > 1:
        mm = sys.maxsize
        for num in nums:
            for ugly in uglys:
                tmp = num * ugly
                if tmp > uglys[-1]:
                    mm = min(tmp, mm)

        uglys.append(mm)
        n -= 1

    return uglys[-1]


# 이후 python .py --test 1 2 3 처럼 사용
if __name__ == "__main__":
    n = int(input())
    print(ugly(n))
