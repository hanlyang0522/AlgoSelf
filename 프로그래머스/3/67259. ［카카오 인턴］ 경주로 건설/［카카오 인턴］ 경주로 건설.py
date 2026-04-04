def solution(board):
    N = len(board)
    ans = 500*N*N
    dirs = [[-1,0], [0,1], [1,0], [0,-1]]
    visit = [[1e9] * N for _ in range(N)]
    
    def dfs(cy, cx, cost, dpast):
        nonlocal N, ans, dirs
        
        #print(cy, cx, cost, dpast)
        
        if cy==N-1 and cx==N-1:
            ans = min(ans, cost)
            return
        
        for i in range(4):
            ny = cy + dirs[i][0]
            nx = cx + dirs[i][1] 
            ncost = cost + 100
            
            #print(ny, nx, ncost)
            
            if i != dpast:
                ncost += 500
            # ncost = cost + (dpast=i ? 100 : 500)
        
            if ny<0 or ny>=N or nx<0 or nx>=N:
                continue
                
            if board[ny][nx]==1:
                continue
                
            if visit[ny][nx] < ncost:
                continue
                
            visit[ny][nx] = ncost
            dfs(ny, nx, ncost, i)  
    
    visit[0][0] = 0
    dfs(0,0,0,1)
    dfs(0,0,0,2)
            
    
    return ans