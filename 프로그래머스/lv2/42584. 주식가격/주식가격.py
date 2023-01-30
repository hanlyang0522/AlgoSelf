def solution(prices):
    st = []  # time, price 저장
    ans = [0 for _ in range(len(prices))]

    for time, price in enumerate(prices):
        while len(st) > 0 and st[-1][1] > price:
            tmp = st.pop()
            ans[tmp[0]] = time - tmp[0]
        st.append([time, price])

    while len(st):
        tmp = st.pop()
        ans[tmp[0]] = time - tmp[0]

    return ans