import sys

f = sys.stdin.readline


def kys(st):
    st2 = sorted(st, key=lambda x: (-x[1], x[2], -x[3], x[0]))
    for i in st2:
        print(i[0])


if __name__ == "__main__":
    N = int(f())
    st = []
    for i in range(N):
        tmp = list(f().split())
        st.append([tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])])

    kys(st)
