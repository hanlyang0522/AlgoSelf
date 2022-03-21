import sys

f = sys.stdin.readline

if __name__ == "__main__":
    num = f()

    l = int((len(num) - 1) / 2)

    t1, t2 = 0, 0
    for i in range(l):
        t1 += int(num[i])
        t2 += int(num[i + l])

    if t1 == t2:
        print("LUCKY")
    else:
        print("READY")
