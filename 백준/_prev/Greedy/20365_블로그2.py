from sys import stdin
import re

leng = int(input())
rblist = stdin.readline()

r_cnt = len(re.findall('R+', rblist))
b_cnt = len(re.findall('B+', rblist))

print(min(r_cnt, b_cnt)+1)
# print(max(S.count("BR"), S.count("RB")) + 1)