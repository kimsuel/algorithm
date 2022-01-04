# 퇴사2

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

n = int(input())
period = []
pay = []
dp = [0] * n


for i in range(n):
    t, p = map(int, input().split())
    period.append(t)
    pay.append(p)


for i in range(n):
    num = i
    check = i + period[i]
    while check <= n:
        dp[i] += pay[num]
        if check == n:
            break
        if check == num:
            check += 1
        num = check
        check = check + period[check]
print(max(dp))
