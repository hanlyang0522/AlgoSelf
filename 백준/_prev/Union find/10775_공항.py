import sys

f = sys.stdin.readline


def findParent(x):
    if parents[x] == x:
        return x
    p = findParent(parents[x])
    parents[x] = p
    return parents[x]


def makeUnion(p1, p2):
    a = findParent(p1)
    b = findParent(p2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def maxGate(G, P):
    global parents
    # parents = {i: i for i in range(G + 1)} # dict로 바꾼다고 더 빨라지진 않음
    parents = [i for i in range(G + 1)]
    cnt = 0

    for i in range(P):
        plane = int(f())

        gate = findParent(plane)

        if gate == 0:
            break
        else:
            cnt += 1
            makeUnion(gate - 1, gate)

    return cnt


if __name__ == "__main__":
    G = int(f())
    P = int(f())

    print(maxGate(G, P))
