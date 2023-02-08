from collections import defaultdict


def solution(string):
    dDi = defaultdict(int)

    for s in string:
        if s == "{":
            tmp = ""
        elif s in ["}", ","]:
            dDi[tmp] += 1
            tmp = ""
        else:
            tmp += s

    dDi = sorted(dDi.items(), key=lambda x: x[1], reverse=True)

    ans = []
    for d in dDi:
        if d[0] == "":
            continue
        ans.append(int(d[0]))

    return ans