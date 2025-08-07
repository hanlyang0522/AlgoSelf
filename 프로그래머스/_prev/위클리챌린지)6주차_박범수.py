import sys
from collections import Counter
f = sys.stdin.readline

def solution(weights, head2head):
    total_list = [[] for _ in range(len(weights))]

    for i in range(len(head2head)):
        # 번호, 몸무게
        total_list[i].append(i+1)
        total_list[i].append(weights[i])

        # 승률
        tmp = Counter(head2head[i])
        print(tmp)
        if tmp['W'] == 0:
            total_list[i].append(0)
        else:
            total_list[i].append(tmp['W']/(tmp['W']+tmp['L']))
        
        # 무거운 복서
        win_cnt = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    win_cnt += 1
        total_list[i].append(win_cnt)

    total_list = sorted(total_list, key=lambda x:(-x[2], -x[3], -x[1], x[0]))

    return [total_list[i][0] for i in range(len(total_list))]

solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])
