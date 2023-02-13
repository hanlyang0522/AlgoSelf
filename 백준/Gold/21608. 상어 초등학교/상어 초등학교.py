"""
빡구현
"""

import sys
from collections import defaultdict

f = sys.stdin.readline

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

def fav(fList): # 인접한 친구 제일 많은 좌표 반환
    di = defaultdict(int) # 좌표별 인접 친구수 저장
    emptyLi = []

    for y in range(n):
        for x in range(n):
            if mat[y][x] in fList: # 해당 좌표가 친구일 경우 인접칸+1
                for dy,dx in dirs:
                    ny,nx = y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n and mat[ny][nx]==0:
                        di[ny,nx]+=1
            elif mat[y][x] == 0:
                emptyLi+=[[y,x]]

    di = sorted(di.items(), key=lambda x:x[1], reverse=True)

    if len(di)!=0: # 인접 친구수가 최대인 좌표들만 반환
        maxCnt = di[0][1]
        maxLi = []
        for d in di:
            if d[1]!=maxCnt:
                break
            maxLi.append(d[0])
        return maxLi
    else: # 인접 친구가 하나도 없을 경우
        return emptyLi


def space(favLi): # 후보 중 공간 제일 많은 리스트 반환
    di = defaultdict(int)

    for y,x in favLi:
        for dy,dx in dirs:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and mat[ny][nx]==0:
                di[y,x]+=1

    if len(di)==0: # 공간 없을 경우
        favLi = sorted(favLi, key=lambda x:(x[0],x[1]))
        return favLi[0]

    di = sorted(di.items(), key=lambda x:x[1], reverse=True)
    # print(di)

    maxCnt = di[0][1]
    maxLi = []
    for d in di:
        if d[1]!=maxCnt:
            break
        maxLi.append(d[0])
    
    maxLi = sorted(maxLi, key=lambda x:(x[0],x[1]))
        
    return maxLi[0]

def calcHap(): # 행복도 계산
    total = 0
    for y in range(n):
        for x in range(n):
            tmp = 0
            for dy,dx in dirs:
                ny,nx = y+dy,x+dx
                if 0<=ny<n and 0<=nx<n and mat[ny][nx] in li2di[mat[y][x]]:
                    if tmp==0:
                        tmp+=1
                    else:
                        tmp*=10
            total += tmp

    return total


if __name__ == "__main__":
    n = int(f())
    li = []
    li2di = {}
    for _ in range(n**2):
        s1, f1, f2, f3, f4 = map(int, f().split())
        li.append([s1, [f1, f2, f3, f4]])
        li2di[s1] = [f1,f2,f3,f4]

    mat = [[0 for _ in range(n)] for __ in range(n)]
    mat[1][1] = li[0][0]

    for s1, fList in li[1:]:
        favLi = fav(fList)
        sy,sx = space(favLi)
        mat[sy][sx] = s1

print(calcHap())