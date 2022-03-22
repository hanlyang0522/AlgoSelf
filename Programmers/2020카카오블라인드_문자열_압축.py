# 자르는건 앞에서부터
# 길이는 len/2
# i 단위로 substr 만들어서 비교


def solution(s):
    if len(s) == 1:
        return 1
    min_len = len(s)

    for i in range(1, len(s) // 2 + 1):
        sub_tot = ""  # 0  # ""
        sub_str = s[:i]
        cnt = 1

        for j in range(i, len(s), i):
            if sub_str == s[j : j + i]:
                cnt += 1

            else:
                if cnt > 1:
                    sub_tot += str(cnt) + sub_str  # len(sub_str) + 1  #
                else:
                    sub_tot += sub_str  # len(sub_str)  #
                sub_str = s[j : j + i]
                cnt = 1

        if cnt > 1:
            sub_tot += str(cnt) + sub_str  # len(sub_str) + 1  # str(cnt) + sub_str
        else:
            sub_tot += sub_str  # len(sub_str)  # sub_str

        # print(sub_tot)
        min_len = min(min_len, len(sub_tot))  # sub_tot)  # len(sub_tot))

    # print()
    print(min_len)
    return min_len


# 7 9 8 14 17
solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
