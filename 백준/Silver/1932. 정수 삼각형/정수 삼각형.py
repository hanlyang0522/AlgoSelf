import sys


f = sys.stdin.readline

# dp로 이전 단계의 최대값만 가져와서 더하기
def maxNum(n, li):
    if n == 1:
        return li[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            # try:
            if j == 0:
                li[i][j] += li[i - 1][0]
            elif j == i:
                li[i][j] += li[i - 1][-1]
            else:
                li[i][j] += max(li[i - 1][j - 1], li[i - 1][j])
            # except:
            #     print(i, j)

    return max(li[-1])


if __name__ == "__main__":
    n = int(f())
    li = []
    for _ in range(n):
        li.append(list(map(int, f().split())))

    print(maxNum(n, li))
