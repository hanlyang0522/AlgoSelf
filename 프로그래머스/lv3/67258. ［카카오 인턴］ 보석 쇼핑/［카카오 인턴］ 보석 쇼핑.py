"""
1. 모든 보석 종류 세기
2. l,r = 0,0
3. hashmap(dict)로 모든 보석 있을 때까지 r+=1
4. 모든 보석 있을 경우, (모든종류-1)까지 l+=1
5. 3~4과정에서 나오는 최소값 = ans
"""

from collections import defaultdict


def solution(gems):
    nGems = len(set(gems))
    di = defaultdict(int)
    l, r = 0, 0
    mLen = len(gems)

    di[gems[0]] += 1

    while l < len(gems):
        if len(di) < nGems and r < len(gems) - 1:
            r += 1
            di[gems[r]] += 1
        else:
            if len(di) == nGems and r - l < mLen:
                mLen = r - l
                ans = [l + 1, r + 1]

            if di[gems[l]] == 1:
                del di[gems[l]]
            else:
                di[gems[l]] -= 1
            l += 1

    return ans