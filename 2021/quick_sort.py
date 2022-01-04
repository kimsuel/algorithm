# quick 정렬은 pivot이라는 임의의 기준값 필요
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    lesser, equal, greater = [], [], []
    for i in list:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort(lesser) + equal + quick_sort(greater)

list = quick_sort(list)

print(list)

# for i in list:
#     print(i, end='\n')

#퀵정렬 최적화 - 하기
