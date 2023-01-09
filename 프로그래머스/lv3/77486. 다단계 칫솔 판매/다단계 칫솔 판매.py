"""
1. enroll-ref를 dict로 만들어서 매 seller마다 타고 올라가기?
--> 판매량이 10000까지라 최대 5번 타고 올라감
--> 최대 10^5 * 5, 시간초과 아님 
"""


def solution(enroll, referral, seller, amount):
    di = {}  # 판매자:추천인
    di2 = {}  # 판매자별 수익금
    for enr, ref in zip(enroll, referral):
        # print(enr, ref)
        di[enr] = ref
        di2[enr] = 0
    # print(di)
    # print(di2)

    for sel, amo in zip(seller, amount):
        amo = amo * 100
        while True:
            ref = di[sel]
            if amo < 10:
                di2[sel] += amo
                break

            ration = amo // 10  # 배분
            di2[sel] += amo - ration  # 나머지

            if ref == "-":
                break

            # 추천인으로 올라감
            amo = ration
            sel = ref

    return [v for k, v in di2.items()]