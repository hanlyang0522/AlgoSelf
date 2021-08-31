from sys import stdin

def solution(word):
    answer = 0
    AEIOU = {'A': 0, 'E': 1, 'I': 2, 'O':3, 'U': 4}
    pos = [781, 156, 31, 6, 1]

    for i in range(len(word)):
        # print(word[i])

        answer += AEIOU[word[i]] * pos[i]




    return answer + len(word)


print(solution(input()))