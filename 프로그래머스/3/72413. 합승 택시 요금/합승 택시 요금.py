from collections import defaultdict, deque

INF = 100000*201
    

def solution(n, s, a, b, fares):
    li =[[INF]*(n+1) for _ in range(n+1)]
    adj_li = defaultdict(list)
    
    for c,d,f in fares:
        li[c][d] = f
        li[d][c] = f
        adj_li[c].append([d,f])
        adj_li[d].append([c,f])
    
    for i in range(n+1):
        li[i][i] = 0
    
    # 1. w-f로 모든 node-node weight 구하기
    for k in range(n+1):
        for n1 in range(n+1):
            for n2 in range(n+1):
                li[n1][n2] = min(li[n1][n2], li[n1][k]+li[k][n2])
                
    # debug
#    for i in range(1, n+1):
#        for j in range(1, n+1):
#            print(li[i][j], end=' ')
#        print()   
    
    
    
    # 2. bfs 돌면서 최적해 업데이트
    dq = deque()
    dq.append([s, 0])
    
    ans = li[s][a]+li[s][b]
    visit = [INF]*(n+1)
    visit[s] = 0
    
    while dq:
        curr, cost = dq.pop()
        
        # 방문시 합승~a,b 비용 계산
        tmp_cost = cost + li[curr][a] + li[curr][b]    
        ans = min(ans, tmp_cost)
        #print(curr, cost, tmp_cost)
        
        for nxt, w in adj_li[curr]:
            if visit[nxt] < cost+w:
                continue
            
            visit[nxt] = cost+w
            dq.append([nxt, cost+w])
    
    
    return ans