"""
참고문헌
- Merge Sort의 복잡도
    - https://ninefloor-design.tistory.com/175
    - https://velog.io/@jimmy48/%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%ACMerge-Sort

"""

import random
import heapq
from collections import deque


def bubbleSort(x):
    """
    인접한 두 원소를 비교해 스왑하는 것을 반복

    시간: O(N^2) / 공간: O(N)
    """
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


def selectionSort(x):
    """
    1~끝까지 훑어서 가장 작은게 1번째,
    2~끝까지 훑어서 가장 작은게 2번째... 순으로
    n-1번 반복

    Unstable sort

    시간: O(N^2) / 공간: O(N)
    """
    for i in range(len(x)):
        minNum = x[i]
        minIdx = i
        for j in range(i, len(x)):
            if x[j] < minNum:
                minNum = x[j]
                minIdx = j
        x[i], x[minIdx] = x[minIdx], x[i]
    return x


def insertionSort(x):
    """
    k번째 원소를 1~k-1까지와 비교해 적절한 위치에 끼워넣고,
    그 뒤의 자료를 한 칸씩 뒤로 밀어내는 방식

    시간: O(N^2) / 공간: O(N)
    """
    for i in range(1, len(x)):
        j, key = i - 1, x[i]
        while x[j] > key and j >= 0:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key
    return x


def shellSort(x):
    """
    Insertion sort의 장점은 살리고 단점은 보완

    정렬한 요소를 그룹으로 나눠 각 그룹별로 insertion sort 수행 후
    그룹을 합치면서 정렬을 반복해 이동 횟수를 줄임

    시간: O(N^1.25~1.5), 최악은 O(N^2) / 공간: O(N)
    """
    N = len(x)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            tmp = x[i]
            j = i - h
            while j >= 0 and x[j] > tmp:
                x[j + h] = x[j]
                j -= h
            x[j + h] = tmp
        h //= 2
    return x


def mergeSort(x):
    """
    원소 개수가 1 또는 0이 될때까지 두 부분으로 쪼개고,
    쪼개서 자른 순서의 역순으로 크기를 비교해 병합

    대표적인 stable sort

    시간: O(NlogN) / 공간: O(2N)
    """
    if len(x) <= 1:
        return x
    left = mergeSort(x[: len(x) // 2])
    right = mergeSort(x[len(x) // 2 :])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
    return x


def heapSort(x):
    """
    원소들을 힙에 모두넣고 힙이 빌 때까지 루트를 출력

    Quick sort에 비해 휴리스틱 없이도 일정한 성능을 보일 수 있다는 것이 장점

    시간: O(NlogN) / 공간: O(n)
    """
    result = []
    heapq.heapify(x)
    while x:
        result.append(heapq.heappop(x))
    return result


def quickSort(x):
    """
    적절한 원소 하나를 pivot으로 삼아 그보다 작은 것은 앞으로, 큰 것은 뒤로 보냄

    pivot을 기준으로 나눠진 좌/우에서 다시 pivot을 정해 정렬을 반복

    list가 정렬되어있을 경우 오히려 느리다는 단점

    시간: 일반적으로 O(NlogN), 최악은 O(N^2) / 공간: O(N)
    """
    if len(x) <= 1:
        return x
    pivot = x[len(x) // 2]
    left, right, equal = [], [], []
    for n in x:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            equal.append(n)

    return quickSort(left) + equal + quickSort(right)


def countingSort(x):
    """
    특정 데이터의 개수(1이 두 개 있다면 2)를 데이터의 값에 대응하는 위치에 저장한 뒤,
    자신의 위치에서 앞에 있던 값을 모두 더한 배열을 만든 뒤,
    거기서 데이터가 들어가야 할 위치를 찾아내는 정렬 알고리즘

    배열을 사용하는 특성상, 정수를 전제로 함

    데이터의 최댓값이 작을수록 빠름

    시간: O(N+k) / 공간: O(N+k)
    """
    di = {}
    for n in x:
        if n in di:
            di[n] += 1
        else:
            di[n] = 1

    result = []
    for n in range(max(x) + 1):
        while n in di and di[n] != 0:
            result.append(n)
            di[n] -= 1

    return result


def radixSort(x):
    """
    자릿수가 있는 데이터(정수, 문자열 등)에서만 수행이 가능하며,
    데이터끼리의 직접적인 비교 없이 정렬을 수행

    자릿수가 적은 4바이트 정수 등에서나 제대로 된 성능을 발휘할 수 있으며,
    자릿수가 무제한에 가까운 문자열 정렬 등에 사용할 경우 오히려 퀵정렬보다 느릴 수 있고,
    부동 소수점의 경우는 부호여부, 지수부, 가수부에 대해 각각 기수정렬을 실행

    시간: O(kN) / 공간: O(N)
    """
    buckets = [deque() for _ in range(10)]
    maxVal = max(x)
    Q = deque(x)
    curIdx = 1

    while maxVal > curIdx:
        while Q:
            num = Q.popleft()
            buckets[(num // curIdx) % 10].append(num)

        for buck in buckets:
            while buck:
                Q.append(buck.popleft())

        curIdx *= 10

    return list(Q)


if __name__ == "__main__":
    n = 20
    li = random.choices(range(1, 20), k=n)
    print(li)

    # liA = bubbleSort(li[:])
    # print(liA)

    # liB = selectionSort(li[:])
    # print(liB)

    # liC = insertionSort(li[:])
    # print(liC)

    # liD = mergeSort(li[:])
    # print(liD)

    # liE = shellSort(li[:])
    # print(liE)

    # liF = heapSort(li[:])
    # print(liF)

    # liG = quickSort(li[:])
    # print(liG)

    # liH = countingSort(li[:])
    # print(liH)

    liI = radixSort(li[:])
    print(liI)
