# 용액
# 5
# -99 -2 -1 4 98

n = int(input())
solution = list(map(int, input().split()))
start = 0
end = n-1
result = abs(solution[start] + solution[end])
cstart = start
cend = end


while start < end:
    tmp = solution[start] + solution[end]
    if abs(tmp) < result:
        cstart = start
        cend = end
        result = abs(tmp)
        if result == 0:
            break
    if tmp > 0:
        end -= 1
    else:
        start += 1
print(solution[cstart], solution[cend])