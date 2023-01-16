from collections import deque


def solution(cacheSize, cities):
    q = deque()
    time = 0

    for city in cities:
        city = city.upper()
        if city in q:
            time += 1
            q.remove(city)
            q.append(city)
        else:
            time += 5
            q.append(city)
            if len(q) > cacheSize:
                q.popleft()

    return time