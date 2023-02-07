"""
이분탐색으로 leaf가 1이고 root가 0이면 불가능
재귀 사용해서 풀려고 했으나 포화이진트리 정하는 부분에서 막힘
--> 이진트리의 크기는 이진수의 길이보다 크거나 같은 2^n-1 중 최소
"""


def check(num):
    if len(num) == 1:
        return int(num[0])

    idx = len(num) // 2
    checkA = check(num[:idx])
    checkB = check(num[idx + 1 :])

    if checkA == -1 or checkB == -1:  # leaf가 불가능
        return -1
    elif num[idx] == 0 and (checkA == 1 or checkB == 1):
        return -1
    elif num[idx] == 0 and checkA == 0 and checkB == 0:
        return 0
    else:
        return 1


def solution(numbers):
    ans = []

    for num in numbers:
        numToBin = bin(num)[2:]
        numToLi = list(map(int, numToBin))
        treeSize = 1
        while treeSize < len(numToLi):
            treeSize = (treeSize + 1) * 2 - 1

        numToLi = [0] * (treeSize - len(numToLi)) + numToLi
        if check(numToLi) >= 0:
            ans.append(1)
        else:
            ans.append(0)

    return ans