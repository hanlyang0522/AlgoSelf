# 시간초과로 실패!
def ansUpdate(room, ans):
    for ppl in room:
        for other in room:
            if ppl != other and other not in ans[ppl-1]:
                ans[ppl-1].append(other)

def solution(enter, leave):
    ans1 = [0 for _ in range(len(enter))]

    idx_in, idx_out = 0, 0
    room = []
    while idx_out < len(leave):
        if idx_in < len(enter):
            room.append(enter[idx_in])
            idx_in += 1
            ansUpdate(room, ans1)

        while idx_out < len(enter) and leave[idx_out] in room: # and idx_out < len(leave):
            room.remove(leave[idx_out])

    # print(ans1)
    ans2 = [len(x) for x in ans1]
    # print(ans2)
    return ans2

# solution([1, 3, 2], [1, 2, 3])
solution([1, 4, 2, 3], [2, 1, 3, 4])
solution([1, 2, 3], [3, 2, 1])
solution([1, 4, 2, 3], [2, 1, 4, 3])