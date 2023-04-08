T = int(input().strip())
for tc in range(1, T + 1):
    n = int(input())
    mat = [list(map(int, input())) for _ in range(n)]
    ans = 0
    
    if n == 1:
        print(f'#{tc} {mat[0][0]}')
        continue

    for y in range(n//2):
        for x in range(n//2-y, n//2+y+1):
            ans += mat[y][x] + mat[n-1-y][x]
    
    for x in range(n):
        ans += mat[n//2][x]
    print(f'#{tc} {ans}')
    