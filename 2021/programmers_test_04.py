# 프린터 - 스택 / 큐

# def solution(priorities, location):
#     answer = 0
#     max_num = max(priorities)
#     string_list = []
#     result = []

#     for i in range(len(priorities)):
#         string_list.append(chr(65+i))
    
#     while True:
#         string = string_list.pop(0)
#         check = priorities.pop(0)
#         if check >= max_num:
#             result.append(string)
#             if len(priorities) == 0:
#                 break
#             max_num = max(priorities)
#         else:
#             string_list.append(string)
#             priorities.append(check)
        
#     answer = result.index(chr(65+location)) + 1

#     return answer

# 다른 사람 풀이
def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    while True:
        check = priorities.pop(0)
        if max_num == check:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_num = max(priorities)
        else:
            priorities.append(check)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

priorities = [1, 1, 9, 1, 1, 1]	
location = 0

print(solution(priorities, location))