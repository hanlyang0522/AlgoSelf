def solution(n, tops):
    a = [0]*n
    b = [0]*n
    MOD = 10007
    
    if tops[0]:
        a[0] = 3
    else:
        a[0] = 2
    b[0] = 1   
    
    for i in range(1, n):
        if tops[i]:
            a[i] = (a[i-1]*3 + b[i-1]*2) % MOD
        else:
            a[i] = (a[i-1]*2 + b[i-1]) % MOD
            
        b[i] = (a[i-1] + b[i-1]) % MOD
        
    return (a[-1] + b[-1]) % MOD