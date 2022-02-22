import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """5 3
1 3 2 3 2
"""
input_lines_2 = """8 5
1 5 4 3 2 4 5 2
"""

input_lines_iter = {1: iter(input_lines_1.split("\n")), 2: iter(input_lines_2.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


if __name__ == "__main__":
    pass
