# weak, dist의 길이가 매우 짧음 --> 완전탐색으로도 가능
# permutation으로 모든 친구의 조합
# 원형 -> 길이를 2배로

from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)  # 취약점 개수
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):  # 시작점
        for perm in list(permutations(dist, len(dist))):  # 친구 조합
            cnt = 1
            pos = weak[start] + perm[cnt - 1]

            for index in range(start, start + length):
                if pos < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[index] + perm[cnt - 1]

            # if cnt == 1:
            #     print(start, perm)
            answer = min(answer, cnt)

    if answer > len(dist):
        # print(-1)
        return -1
    # print(answer)
    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
