string = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
for tc in range(1, T + 1):
    st = input()
    ans = 0
    for i in range(len(st)):
        if st[i] == string[i]:
            ans += 1
        else:
            break
    print(f'#{tc} {ans}')
