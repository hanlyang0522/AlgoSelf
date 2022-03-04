import argparse
from unicodedata import digit

from cv2 import sort

parser = argparse.ArgumentParser()
parser.add_argument("--test", type=int, default=0)
args = parser.parse_args()

input_lines_1 = """K1KA5CB7
"""
input_lines_2 = """AJKDLSI412K4JSJ9D
"""

input_lines_iter = {0: iter(input_lines_2.split("\n")), 1: iter(input_lines_2.split("\n"))}


# 이후 python .py --test 1 2 3 처럼 사용
def input():
    return next(input_lines_iter[args.test])


def string_sort(st):
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total = 0
    st = sorted(st)

    for s in st:
        if s in digit:
            total += int(s)
        else:
            print(s, end="")
    print(total)


if __name__ == "__main__":
    S = input()

    string_sort(S)
