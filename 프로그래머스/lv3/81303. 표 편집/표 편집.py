"""
1. 총 x합이 10^6, n은 2*10^5라 브루트포스는 초과1
2. 그런데 list의 값 변경은 O(1)이라 가능할듯 -> idx랑 list 사용
--> 시간초과!

1. linked list로 해결하기
"""


class Node:
    def __init__(self, left=None, right=None) -> None:
        self.remove = False
        self.left = left
        self.right = right


def solution(n, k, cmd):
    lli = [Node(i - 1, i + 1) for i in range(n)]
    lli[0].left = None
    lli[-1].right = None

    stack = []
    idx = k

    for c in cmd:
        if c[0] == "U":
            _, move = c.split()
            for _ in range(int(move)):
                idx = lli[idx].left
        elif c[0] == "D":
            _, move = c.split()
            for _ in range(int(move)):
                idx = lli[idx].right
        elif c[0] == "C":
            lli[idx].remove = True
            stack.append(idx)

            l, r = lli[idx].left, lli[idx].right
            if l or l == 0:
                lli[l].right = r
            if r:
                lli[r].left = l
                idx = r
            else:  # 마지막일 경우
                idx = l
        else:
            tmp = stack.pop()
            lli[tmp].remove = False

            l, r = lli[tmp].left, lli[tmp].right

            if l:
                lli[l].right = tmp
            if r:
                lli[r].left = tmp

    ans = ""
    for i in lli:
        if i.remove:
            ans += "X"
        else:
            ans += "O"
    return ans