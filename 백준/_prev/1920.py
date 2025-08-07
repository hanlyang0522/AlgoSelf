import sys

def b_search(li, target):
    left, right = 0, len(li)-1
    
    while left <= right:
        mid = (left+right)//2

        if li[mid] == target:
            return True
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


int(sys.stdin.readline())
list_pool = list(map(int, sys.stdin.readline().split()))
list_pool.sort()
# print(list_pool)

int(sys.stdin.readline())
num_iter = list(map(int, sys.stdin.readline().split()))
# print(num_iter)

for num in num_iter:
    if b_search(list_pool, num):
        print('1')
    else:
        print('0')