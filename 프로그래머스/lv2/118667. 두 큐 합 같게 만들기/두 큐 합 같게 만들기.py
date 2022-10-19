# 1. tree 형태로 왼pop / 오른pop 가지치기
# 2. queue에 넣어두고 popleft, 왼pop/오른pop 다시 append
# 3. history 만들어서 중복은 제거
# --> 시간초과로 43.3점
# 1. 매번 합 비교해서 크면 pop, 작으면 push
# --> 시간초과 66.7점
# 1. deque 사용, sum은 처음에만 계산
from collections import deque


def solution(q1, q2):
    q1, q2 = deque(q1), deque(q2)
    s1, s2 = sum(q1), sum(q2)
    target = (s1 + s2) / 2
    if target % 1 == 0.5:
        return -1

    for i in range(len(q1) * 3):
        if s1 == target:
            return i
        if s1 > s2:
            num = q1.popleft()
            q2.append(num)
            s1 -= num
            s2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            s2 -= num
            s1 += num
    return -1