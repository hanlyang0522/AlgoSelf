import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """02984
"""
input_lines_2 = """5030291
"""

input_lines_iter = {0: iter(input_lines_2.split("\n")), 1: iter(input_lines_2.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def porm(n):
    result = 0

    for i in n:
        print(i)
        if i == "0" or i == "1" or result == 0:
            result += int(i)
        else:
            result *= int(i)

    return result


if __name__ == "__main__":
    n = input()

    print(porm(n))
