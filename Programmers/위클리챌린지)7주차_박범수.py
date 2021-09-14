def ansUpdate(room, ans):
    for i in range(0, len(ans)):
            if i+1 in room:
                for ppl in room:
                    if ppl not in ans[i] and ppl != i+1:
                        ans[i].append(ppl)


def solution(enter, leave):
    ans1 = [[] for _ in range(len(enter))]

    idx_in, idx_out = 0, 0
    room = []
    while idx_out < len(leave):
        if idx_in < len(enter):
            room.append(enter[idx_in])
            idx_in += 1
            print(room)
            ansUpdate(room, ans1)

        if leave[idx_out] in room: # and idx_out < len(leave):
            room.remove(leave[idx_out])
            idx_out += 1
            print(room)
            ansUpdate(room, ans1)


    print(ans1)
    ans2 = [len(x) for x in ans1]
    print(ans2)
    return ans2

# solution([1, 3, 2], [1, 2, 3])
solution([1, 4, 2, 3], [2, 1, 3, 4])
solution([1, 2, 3], [3, 2, 1])