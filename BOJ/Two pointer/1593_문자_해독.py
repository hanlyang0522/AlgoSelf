import sys

f = sys.stdin.readline

g, lS = map(int, f().split())
W = f().strip()
S = f().strip()

strcnt_W = [0 for i in range(52)]

for w in W:
    if "a" <= w <= "z":
        strcnt_W[ord(w) - ord("a")] += 1
    else:
        strcnt_W[ord(w) - ord("A") + 26] += 1

cnt = 0
strcnt_S = [0 for i in range(52)]

for s in S[0:g]:
    if "a" <= s <= "z":
        strcnt_S[ord(s) - ord("a")] += 1
    else:
        strcnt_S[ord(s) - ord("A") + 26] += 1

if strcnt_S == strcnt_W:
    cnt += 1

for idx in range(g, lS):
    tmp_del, tmp_add = S[idx - g], S[idx]

    # add last alp
    if "a" <= tmp_add <= "z":
        strcnt_S[ord(tmp_add) - ord("a")] += 1
    else:
        strcnt_S[ord(tmp_add) - ord("A") + 26] += 1

    # sub first alp
    if "a" <= tmp_del <= "z":
        strcnt_S[ord(tmp_del) - ord("a")] -= 1
    else:
        strcnt_S[ord(tmp_del) - ord("A") + 26] -= 1

    if strcnt_S == strcnt_W:
        cnt += 1

print(cnt)
