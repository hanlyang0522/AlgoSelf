import sys

f = sys.stdin.readline

g, lS = map(int, f().split())
W = f().strip()
S = f().strip()
# print(W, S)


def StrCnt(string):
    wli = [0 for i in range(52)]

    for w in string:
        if "a" <= w <= "z":
            wli[ord(w) - ord("a")] += 1
        else:
            wli[ord(w) - ord("A") + 26] += 1

    return wli


strcnt_W = StrCnt(W)
cnt = 0
# print(strcnt_W)

for idx in range(4, lS + 1):
    substr = S[idx - 4 : idx]
    # print(substr)
    if strcnt_W == StrCnt(substr):
        cnt += 1

print(cnt)
