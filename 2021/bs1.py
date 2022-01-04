# 숫자 카드
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))


for i in m_list:
    left = 0
    right = n-1
    check = True
    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == i:
            print(1, end=' ')
            check = False
            break
        elif n_list[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    if check:
        print(0, end=' ')