from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)
        
    for key in info_dict.keys():
        info_dict[key].sort()
    # print(info_dict)

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]    
        
        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)
        # print(tmp_q, query_score)
        
        # if tmp_q in info_dict:
        scores = info_dict[tmp_q]
        if len(scores) > 0:
            start, end = 0, len(scores)
            while end >  start:
                mid = (start + end) // 2
                if scores[mid] >= query_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scores) - start)
        else:
            answer.append(0)
            
    return answer