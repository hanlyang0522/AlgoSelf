import sys

f = sys.stdin.readline


n, li = int(f()), list(map(int, f().split()))
st = []
ans = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
    while len(st) > 0 and st[-1] <= li[i]:
        st.pop()

    if len(st) > 0:
        ans[i] = st[-1]
    else:
        ans[i] = -1

    st.append(li[i])

for i in range(n - 1):
    print(ans[i], end=" ")
print(ans[-1])