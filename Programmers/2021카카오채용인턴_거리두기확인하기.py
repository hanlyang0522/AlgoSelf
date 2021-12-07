def ifDist(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                if check(place, y, x):  # 거리두기 x시 true
                    return 0

    # 모두 거리두기 지킬 경우
    return 1


def check(place, y, x):
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            cy, cx = y + dy, x + dx  # 현재 위치
            if (abs(dy) + abs(dx) >= 3) or (dy == 0 and dx == 0):  # 맨해튼 거리 <= 2
                continue
            if cy < 0 or cy > 4 or cx < 0 or cx > 4:  # 대기실 벗어날 경우
                continue
            if place[cy][cx] == "P":  # 근처에 지원자가 있을 경우
                if [dy, dx] in ([-1, 0], [1, 0], [0, -1], [0, 1]):  # 바로 근접
                    return True
                elif abs(dy) == 2 or abs(dx) == 2:  # 한 자리 띄고
                    if (
                        (dy == -2 and place[y - 1][x] != "X")
                        or (dy == 2 and place[y + 1][x] != "X")
                        or (dx == -2 and place[y][x - 1] != "X")
                        or (dx == 2 and place[y][x + 1] != "X")
                    ):
                        return True
                elif place[cy][x] != "X" or place[y][cx] != "X":  # 대각선 위치
                    return True
    return False


def solution(places):
    answer = []

    for place in places:
        answer.append(ifDist(place))
    print(answer)

    return answer


solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)
