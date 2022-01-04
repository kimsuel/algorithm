# 더 맵게 - heap(힙)
# sort 사용하면 시간초과 남
# heapQ 사용하라고 함

import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) # list to heapq
    
    while scoville[0] < k:
        if len(scoville) > 1:
            answer += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second*2)
        else:
            return -1
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))



# def solution(scoville, k):
#     answer = 0
#     result_list = sorted(scoville)

#     while True:
#         result_list = sorted(result_list)
#         if result(result_list, k):
#             break
#         result_list = formula(result_list[0], result_list[1], result_list)
#         answer += 1
        
#     return answer

# def result(result_list, k):
#     count = 0
#     for sco in result_list:
#         if sco > k:
#             count += 1
#     if count == len(result_list):
#         return True
#     else:
#         return False

# def formula(i, j, result_list):
#     x = i + (j*2)
#     result_list.remove(i)
#     result_list.remove(j)
#     result_list.append(x)
#     return result_list
