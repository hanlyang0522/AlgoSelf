import sys

f = sys.stdin.readline


def maxMeet(n, meetings):
    cnt = 0
    prev_end = 0

    for start, end in meetings:
        if start >= prev_end:
            cnt += 1
            prev_end = end

    return cnt


if __name__ == "__main__":
    n = int(f())
    meetings = []
    for _ in range(n):
        meetings.append(list(map(int, f().split())))

    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))  # 종료시간을 기준으로 정렬
    # print(meetings)
    print(maxMeet(n, meetings))
