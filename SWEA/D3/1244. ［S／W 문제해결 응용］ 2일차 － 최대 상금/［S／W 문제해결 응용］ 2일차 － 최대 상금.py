from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, (input().split()))

    visit = set()
    visit.add((N, 0))

    q = deque()
    q.append((N, 0))

    ANS = 0

    while q:
        num, depth = q.pop()

        if depth == K:
            ANS = max(ANS, num)
            continue

        num = list(str(num))
        L = len(num)

        for i in range(L - 1):
            for j in range(i + 1, L):
                num[i], num[j] = num[j], num[i]

                NN = int("".join(num))

                if (NN, depth + 1) not in visit:
                    q.append((NN, depth + 1))
                    visit.add((NN, depth + 1))

                num[i], num[j] = num[j], num[i]

    print(f"#{test_case} {ANS}")