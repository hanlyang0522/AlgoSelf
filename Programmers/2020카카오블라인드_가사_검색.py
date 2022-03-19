# 1. words 정렬
# 2. word-query 대소비교하는 함수 작성
# 3. query 해당하는 첫 idx ~ 끝 idx 찾기



def binSearch(words, query, mode):
    query_ = query.replace('?','')
    length = len(query) - len(query_)
    if length:
        if query[0]=='?':
            pos = 'front'
        else:
            pos = 'back'
    l, r = 0, len(words)-1

def wqComp(word, query_, length, pos):
    if pos=='front':
        if word[:len(query_)]==query_ and len(word)>=len(query_)+length:
            return True
    else:
        if word[]

    return False


def solution(words, queries):
    answer = []

    words = sorted(words)
    print(words)

    for query in queries:
        start = binSearch(words, query, 'min')
        end = binSearch(words, query, 'max')
        answer.append(end-start)

    return answer


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)  # [3, 2, 4, 1, 0]
