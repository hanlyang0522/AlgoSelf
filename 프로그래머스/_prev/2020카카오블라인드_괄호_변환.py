def trans(string):
    # 1. 빈 문자열일 경우 빈 문자열 반환
    if string == "":
        return ""

    # 2. 균형잡힌 u,v로 분리
    u, v = sep_uv(string)

    # 3. 올바른 u
    if is_right(u):
        return u + trans(v)
    # 4. 안 올바른 u
    else:
        tmp = "(" + trans(v) + ")"

        for s in u[1:-1]:
            if s == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp


def sep_uv(string):
    cnt = 0
    for i in range(len(string)):
        if string[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            u = string[: i + 1]
            v = string[i + 1 :]
            break

    return u, v


def is_right(string):
    while string:
        if "()" in string:
            string = string.replace("()", "")
        else:
            return False
    return True


def solution(p):
    return trans(p)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
# print(is_right("(()())()"))
# print(is_right("()))((()"))
# print(is_right(")(()()"))
# print(is_right("))((()"))
