"""
n = 10^6이라 O(N) ~ O(NlogN)으로 풀어야함
"""


def solution(topping):
    s1 = set()
    s2 = set()
    li1 = [0 for _ in range(len(topping))]
    li2 = [0 for _ in range(len(topping))]
    
    for i in range(len(topping)):  # O(N)
        s1.add(topping[i])  # O(1)
        li1[i] = len(s1)  # O(1)

        s2.add(topping[-(i + 1)])
        li2[-(i + 1)] = len(s2)

    cnt = 0
    
    for i in range(len(topping) - 1):  # O(N)
        if li1[i] == li2[i + 1]:
            cnt += 1

    return cnt