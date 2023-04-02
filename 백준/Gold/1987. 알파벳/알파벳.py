import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
alpha = [False] * 26
max_ = 1
d = [(1,0), (-1,0), (0,1), (0,-1)]

def DFS(x, y, cnt):
    global max_
    max_ = max(max_, cnt)
    
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        
        if 0 <= nx < r and 0 <= ny < c:
            if not alpha[board[nx][ny]]:
                alpha[board[nx][ny]] = True
                DFS(nx,ny,cnt+1)
                alpha[board[nx][ny]] = False
                    
alpha[board[0][0]] = True
DFS(0,0,max_)
print(max_)