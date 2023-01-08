from itertools import product


def solution(users, emoticons):

    # 가입자, 금액
    max_n, max_cost = 0, 0

    # 가능한 모든 할인율
    for sp in product([10, 20, 30, 40], repeat=len(emoticons)):
        # 가입자수, 매출액 계산
        n, cost = 0, 0

        # 유저별 가입여부, 구매비용 계산
        for user in users:
            total = 0

            for i in range(len(sp)):
                if sp[i] >= user[0]:
                    total += emoticons[i] * (100 - sp[i]) / 100

            if total >= user[1]:
                n += 1
            else:
                cost += total

        if n > max_n:
            max_n = n
            max_cost = cost
        elif n == max_n:
            max_cost = max(max_cost, cost)

    return [max_n, max_cost]