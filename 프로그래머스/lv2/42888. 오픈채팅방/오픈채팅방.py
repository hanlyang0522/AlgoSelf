def solution(record):
    di = {}
    ans = []

    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            di[rec[1]] = rec[2]
        elif rec[0] == "Change":
            di[rec[1]] = rec[2]

    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            tmp = di[rec[1]] + "님이 들어왔습니다."
        elif rec[0] == "Leave":
            tmp = di[rec[1]] + "님이 나갔습니다."
        else:
            continue
        ans.append(tmp)

    return ans