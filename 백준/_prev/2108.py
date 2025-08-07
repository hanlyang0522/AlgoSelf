import sys
import statistics
from collections import Counter

times = int(sys.stdin.readline())
num = []

for i in range(times):
    num.append(int(sys.stdin.readline()))

print(num)

def my_mean(num_list):
    return round(statistics.mean(num_list))

def my_median(num_list):
    return statistics.median(num_list)

def my_freq(num_list):
    c = Counter(num_list)
    c = sorted(c.items(), key=lambda x:x[1])
    return c[0][0]

def my_range(num_list):
    return max(num_list) - min(num_list)

print(my_mean(num))
print(my_median(num))
print(my_freq(num))
print(my_range(num))
