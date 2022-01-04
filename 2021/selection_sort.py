n = int(input())
sort = [] # [5,4,3,2,1]

# list 받기
for i in range(n):
    sort.append(int(input())) # 64 24 12 22 11
    

# 선택정렬 구현하기 ( 제일 작은 값이 들어있는 index 구하기 )
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if sort[j] < sort[min]:
            min = j
    sort[i], sort[min] = sort[min], sort[i]

            
        
    
#list 안에 변수들을 한줄씩 출력하기
for i in sort:
    print(i, end='\n')
                                    


