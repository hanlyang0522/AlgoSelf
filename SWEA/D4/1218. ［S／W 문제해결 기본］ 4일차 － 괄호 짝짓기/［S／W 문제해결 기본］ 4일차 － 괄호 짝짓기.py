T = 10

for tc in range(1, T + 1):
    N = int(input())

    if N % 2 == 1:
        print(f"#{tc} {0}")
        
        li = str(input())
        continue

    q = []
    flag = True

    li = str(input())

    for i in range(len(li)):
        if li[i] in ['(', '{', '[', '<']:
            q.append(li[i])
        else:
            if (li[i] == ')' and q[-1] != '(') or (li[i] == '}' and q[-1] != '{') or (
                    li[i] == ']' and q[-1] != '[') or (li[i] == '>' and q[-1] != '<'):
                flag = False
                break
            else:
                q.pop()

    if flag:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
