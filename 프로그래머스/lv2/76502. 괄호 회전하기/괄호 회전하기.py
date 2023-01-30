from collections import deque


def validCheck(string):
    st = []
    for s in string:
        if s in ["(", "[", "{"]:
            st.append(s)
        elif len(st) == 0:
            return False
        else:
            tmp = st.pop()
            if not (
                (tmp == "(" and s == ")") or (tmp == "[" and s == "]") or (tmp == "{" and s == "}")
            ):
                return False

    return len(st) == 0


def solution(s):
    s = deque(s)

    cnt = 0
    for i in range(len(s)):
        s.rotate()
        if validCheck(s):
            cnt += 1

    return cnt