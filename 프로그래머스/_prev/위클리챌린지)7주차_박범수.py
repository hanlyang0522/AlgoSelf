def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    e_list = [] # 현재 room에 남아있는 사람
    l_queue = [] # 나갈 차례가 된 사람

    for e, l in zip(enter, leave):
        e_list.append(e)
        l_queue.append(l)

        while len(l_queue) != 0 and l_queue[0] in e_list:
            l_tmp = l_queue[0]
            # 나갔으니 제거
            l_queue.pop(0)
            e_list.remove(l_tmp)

            # 나간 사람은 room에 남아있는 사람 수만큼 만남
            if len(e_list) != 0:
                answer[l_tmp - 1] += len(e_list)

            # 남은 사람은 현재 나간사람을 만남
            for e_p in e_list:
                answer[e_p - 1] += 1

    print(answer)
    return answer


solution([1, 4, 2, 3], [2, 1, 3, 4])
solution([1, 2, 3], [3, 2, 1])
solution([1, 4, 2, 3], [2, 1, 4, 3])