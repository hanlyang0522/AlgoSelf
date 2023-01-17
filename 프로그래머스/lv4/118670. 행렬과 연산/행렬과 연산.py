from collections import deque


def solution(rc, operations):
    left = deque()
    mid = deque()
    right = deque()

    for i in range(len(rc)):
        left.append(rc[i][0])
        right.append(rc[i][-1])

        midQueue = deque()
        for j in range(1, len(rc[0]) - 1):
            midQueue.append(rc[i][j])
        mid.append(midQueue)

    for op in operations:
        if op == "ShiftRow":
            left.rotate()
            mid.rotate()
            right.rotate()
        else:
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())

    for i in range(len(rc)):
        rc[i][0] = left.popleft()
        rc[i][-1] = right.popleft()

        for j in range(1, len(rc[0]) - 1):
            rc[i][j] = mid[i].popleft()
    return rc
