# 2018
# 수 들의 합 5

n = int(input())

count = 1
start = 0
end = 1
n_sum = 1

while start < n/2 + 1:
    if n_sum < n:
        end += 1
        n_sum += end
    elif n_sum == n:
        count += 1
        end += 1
        n_sum -= start
        n_sum += end
        start += 1
    else:
        n_sum -= start
        start += 1

print(count)
