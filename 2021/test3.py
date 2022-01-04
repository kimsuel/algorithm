# n = 3
# list = [5,3,4,1,2,6,7,8] -> [1,2,3,4,5,6,7,8]
# 1 2 4 5 6 7 8 9

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
left = 0
right = len(n_list) -1

while left <= right:
    mid = (left + right) // 2
    if n_list[mid] == n:
        print(1)
        break
    elif n_list[mid] > n:
        right = mid - 1
    else:
        left = mid + 1
else:
    print(0) 