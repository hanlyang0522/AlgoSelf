import sys
from itertools import permutations

f = sys.stdin.readline

L, C = map(int, f().split())

lett = list(f().split())
lett.sort()


# 모음1개, 자음2개
def vcheck(word):
    vcnt = 0
    for w in word:
        if w in ["a", "e", "i", "o", "u"]:
            vcnt += 1
    if vcnt < 1 or L - vcnt < 2:
        return False
    else:
        return True


# 브루트포스
def search(word, cnt):
    global lett
    global L

    if len(word) > L:
        return

    if len(word) == L and vcheck(word):
        print(word)
        return

    if cnt < C:
        search("".join(word + lett[cnt]), cnt + 1)
        search(word, cnt + 1)


search("", 0)
