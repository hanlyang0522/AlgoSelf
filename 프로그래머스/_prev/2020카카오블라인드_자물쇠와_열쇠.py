# 1. M,N 크기 모두 20이라 최대 400회 비교 --> 완전탐색 가능?
# 2. key를 90도씩 4번 회전해서 모두 검증

import copy


def solution(key, lock):
    M, N = len(key), len(lock)
    num_hole = 0
    for i in range(N):
        num_hole += lock[i].count(0)

    for i in range(4):
        # 1. 90도 회전한 key 생성
        new = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                new[j][M - i - 1] = key[i][j]
        key = copy.deepcopy(new)  # 2중리스트 깊은 복사

        # 2. lock은 -M+1 ~ N-1 stride
        for ly in range(-M + 1, N):
            for lx in range(-M + 1, N):

                # 3. key는 0 ~ M-1 stride, 홈 채우는지 검사
                flag = True
                num_check = 0
                for ky in range(M):

                    if not flag:
                        break

                    for kx in range(M):
                        # 3-1. 범위 넘어갈 경우 건너뜀
                        if ly + ky < 0 or ly + ky >= N or lx + kx < 0 or lx + kx >= N:
                            continue

                        # 3-2. 홈/돌기가 안 겹치는지, 홈은 다 채우는지 확인
                        if key[ky][kx] == lock[ly + ky][lx + kx]:
                            flag = False
                            break
                        elif key[ky][kx] == 1 and lock[ly + ky][lx + kx] == 0:
                            num_check += 1

                if flag and num_hole == num_check:
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # True
