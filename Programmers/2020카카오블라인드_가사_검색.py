# 이중for문 돌려서 시작과 끝 찾기?? --> 효율성 탈락!
# 그러면 bisect로 시작과 끝을 찾자!
# ?가 앞에 있을 경우는? --> 문자 전체를 뒤집어서

# 1. words 정렬
# 2. word-query 대소비교하는 함수 작성
# 3. query 해당하는 첫 idx ~ 끝 idx 찾기
import bisect


def binSearch(words, query, mode):
    query_ = query.replace("?", "")
    length = len(query) - len(query_)
    if length:
        if query[0] == "?":
            pos = "front"
        else:
            pos = "back"
    l, r = 0, len(words) - 1


def wqComp(word, query_, length, pos):
    if pos == "front":
        if word[: len(query_)] == query_ and len(word) >= len(query_) + length:
            return True
    else:
        return -1
        # if word[]

    return False


def solution(words, queries):
    answer = []
    words = sorted(set(words))
    print(words)

    for query in queries:
        start = binSearch(words, query, "min")
        end = binSearch(words, query, "max")
        answer.append(end - start)

    return answer


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)  # [3, 2, 4, 1, 0]
