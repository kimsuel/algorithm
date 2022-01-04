# 값 받기

# swap을 이용한 최적화 
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))


for i in range(n):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            tmp = list[j]
            list[j] = list[j+1]
            list[j+1] = tmp


for i in range(n):
    print(list[i], end='\n')


# 추가 최적화
# - 마지막으로 앞뒤 자리 비교가 있었던 index를 기억하여
# - 다음 패스에서는 그 자리 전까지만 정렬

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

end = n -1
while end > 0:
    last_swap = 0
    for i in range(end):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            last_swap = i
    end = last_swap


for i in range(n):
    print(list[i], end='\n')
