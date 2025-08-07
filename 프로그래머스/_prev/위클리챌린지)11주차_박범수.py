def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    if len(rectangle) > 1:
        return 0

    x, y, X, Y = rectangle[0]

    right = X - characterX + X - itemX
    left = characterX - x + itemX - x
    # print(left, right)
    if left < right:
        answer += left
    else:
        answer += right

    up = Y - characterY + Y - itemY
    down = characterY - y + itemY - y
    # print(down, up)
    if down < up:
        answer += down
    else:
        answer += up

    return answer


solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
solution([[1, 1, 5, 7]], 1, 1, 4, 7)
solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10)
solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)
