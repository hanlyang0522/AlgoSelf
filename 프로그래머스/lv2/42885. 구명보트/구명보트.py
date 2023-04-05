'''
문제를 잘 읽자!! 최대 2명까지만 탑승 가능
'''

def solution(ppl, lmt):
    ppl = sorted(ppl)

    cnt = 0
    l, r = 0, len(ppl) - 1

    while l <= r:
        # 초과할 경우 무거운 사람만 탑승
        if ppl[l] + ppl[r] > lmt:
            r -= 1
        # 아닐 경우 모두 탑승
        else:
            r -= 1
            l += 1
        cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
