# 숫자 카드 2
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
n_counts = Counter(n_list)
n_list = sorted(list(set(n_list)))
m = int(input())
m_list = list(map(int, input().split()))
result = []

for i in m_list:
    start = 0
    last = len(n_list)-1
    check = True

    while start <= last:
        mid = (start + last) // 2
        if n_list[mid] == i:
            result.append(n_counts[i])
            check = False
            break
        elif n_list[mid] > i:
            last = mid - 1
        else:
            start = mid + 1

    if check:
        result.append(0)

for i in result:
    print(i, end=' ')
