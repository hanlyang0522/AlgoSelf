T = int(input().strip())
for test_case in range(1, T + 1):
    num = int(input())
    ans = num-1
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            if i + num/i - 2 < ans:
                ans = int(i + num/i - 2)
    print(f'#{test_case} {ans}')

