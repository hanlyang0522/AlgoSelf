def solution(board):
    ans = board[0][0]
    
    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                board[y][x] += min(board[y-1][x], board[y][x-1], board[y-1][x-1])
                ans = max(board[y][x], ans)
                
    return ans**2