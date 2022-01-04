n = int(input())
list = []

for i in range(n):
    list.append(int(input()))


for i in range(1, n):
    for j in range(i, 0, -1):
        if list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]


for i in range(n):
    print(list[i], end='\n')


#최적화 - end 이용
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))


for i in range(1, n):
    j = i
    while j > 0 and list[j-1] > list[j]:
        list[j-1], list[j] = list[j], list[j-1]
        j -= 1


for i in range(n):
    print(list[i], end='\n')