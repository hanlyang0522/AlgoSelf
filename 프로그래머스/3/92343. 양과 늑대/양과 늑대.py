from collections import defaultdict

def solution(info, edges):
    adj = defaultdict(list)
    
    for u,v in edges:
        adj[u].append(v)
        
    ans = 0
        
    def dfs(curr, wolf, sheep, possible):
        nonlocal ans
        
        if info[curr] == 0:
            sheep += 1
        else: 
            wolf += 1
            
        if wolf >= sheep:
            return 
        
        ans = max(ans, sheep)
        
        
        for child in adj[curr]:
            possible.add(child)
            
        #print(curr, wolf, sheep, possible)
            
        for child in possible:
            future = possible - {child}
            dfs(child, wolf, sheep, future)
        
        
    dfs(0,0,0,set())
    
    return ans