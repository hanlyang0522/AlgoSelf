from collections import defaultdict, deque

INF  = 1e9

def solution(N, road, K):
    li = defaultdict(list)
    
    for u,v,w in road:
        li[u].append([v,w])
        li[v].append([u,w])
    
    ans = set()
    
    dq = deque()
    dq.append([1, 0])
    
    visit = [INF] * (N+1)
    visit[1] = 0
    
    
    
    while dq:
        curr, cost = dq.pop()
        ans.add(curr)
        #print(curr)
        
        for nxt, w in li[curr]:
            ncost = cost + w
            
            if visit[nxt] < ncost or ncost > K:
                continue
            
            visit[nxt] = ncost            
            dq.append([nxt, ncost])
    
    
    

    

    return len(ans)