"""
1. q에 카드 리스트 저장
2. while q:
    같은 짝끼리 뒤집기
3. 단 [r,c]가 카드일 경우 [r,c]부터 시작할것
    종료좌표와 같은 카드가 있을 경우 우선으로 탐색(n=8이라 가능)
--> 결국 이동방법을 계산 못했는데 bfs로 탐색하는거였음..
    2차원 배열에서 가중치가 1인 상황에서의 최단거리 = bfs
"""
from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

board = []
dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def bfs(sy, sx, ey, ex):
    q = deque()
    q.append((sy, sx))
    visit = [[int(1e9) for _ in range(4)] for __ in range(4)]
    visit[sy][sx] = 0

    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            return visit[y][x]

        # 일반 이동
        for dy, dx in dirs:
            _y, _x = y + dy, x + dx
            if 0 <= _y < 4 and 0 <= _x < 4 and visit[_y][_x] > visit[y][x] + 1:
                visit[_y][_x] = visit[y][x] + 1
                q.append((_y, _x))

        # 컨트롤 이동
        for dy, dx in dirs:
            _y, _x = y + dy, x + dx
            while 0 <= _y + dy < 4 and 0 <= _x + dx < 4 and board[_y][_x] == 0:
                _y, _x = _y + dy, _x + dx
            if 0 <= _y < 4 and 0 <= _x < 4 and visit[_y][_x] > visit[y][x] + 1:
                visit[_y][_x] = visit[y][x] + 1
                q.append((_y, _x))


def solution(boardInput, r, c):
    global board
    board = boardInput

    cards = defaultdict(list)
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                cards[board[y][x]].append((y, x))

    ans = int(1e9)
    for cardOrder in list(permutations(cards.keys())):
        board = deepcopy(boardInput)
        cnt = 0
        y, x = r, c
        for card in cardOrder:
            left = bfs(y, x, cards[card][0][0], cards[card][0][1])
            right = bfs(y, x, cards[card][1][0], cards[card][1][1])

            if left < right:
                cnt += left
                cnt += bfs(
                    cards[card][0][0],
                    cards[card][0][1],
                    cards[card][1][0],
                    cards[card][1][1],
                )
                y, x = cards[card][1]
            else:
                cnt += right
                cnt += bfs(
                    cards[card][1][0],
                    cards[card][1][1],
                    cards[card][0][0],
                    cards[card][0][1],
                )
                y, x = cards[card][0]
            board[cards[card][0][0]][cards[card][0][1]] = 0
            board[cards[card][1][0]][cards[card][1][1]] = 0
            cnt += 2
        ans = min(ans, cnt)

    return ans