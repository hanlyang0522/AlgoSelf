# 자르는건 앞에서부터
# 길이는 len/2


def solution(s):
    # print(len(s))
    l = len(s)
    min_len = l

    for i in range(1, l // 2 + 1):
        tmp_s = s[:i]
        tmp_len = i
        repeat = False
        # print(tmp_s)

        for j in range(i, l, i):
            # print(s[j : j + i])
            if s[j : j + i] == tmp_s:
                if repeat == False:
                    tmp_len += 1
                    repeat = True
            else:
                tmp_s = s[j : j + i]
                tmp_len += len(tmp_s)
                repeat = False

        min_len = min(min_len, tmp_len)

    # print()
    print(min_len)
    return min_len


# solution("aabbaccc")
# solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
