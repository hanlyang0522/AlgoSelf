def solution(record):
    di = {}
    msg = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            di[rec[1]] = rec[2]
        elif rec[0] == "Change":
            di[rec[1]] = rec[2]

    ans = []
    for rec in record:
        rec = rec.split()
        if rec[0] == "Change":
            continue
        ans.append(di[rec[1]] + msg[rec[0]])

    return ans
