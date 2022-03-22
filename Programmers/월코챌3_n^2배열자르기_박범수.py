# def solution(n, left, right):
#     ans = []
#     mat = [[0] * n for i in range(n)]

#     for i in range(n):
#         for j in range(n):
#             mat[i][j] = max(i, j) + 1
#     # print(mat)

#     lq, lr = left // n, left % n
#     rq, rr = right // n, right % n
#     # print(lq, lr, rq, rr)

#     for y in range(lq, rq + 1):
#         for x in range(n):
#             if y == lq and x < lr:
#                 continue
#             if y == rq and x > rr:
#                 break

#             ans.append(mat[y][x])

#     # print(ans)
#     return ans


def solution(n, left, right):
    ans = []
    for i in range(left, right + 1):
        ans.append(max(i // n, i % n) + 1)

    print(ans)
    return ans


solution(3, 2, 5)
solution(4, 7, 14)
