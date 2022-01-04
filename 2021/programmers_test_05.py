# 체육복
# 여러 테스트 케이스에서 몇개 통과못함

# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     lost = sorted(lost)
#     reserve = sorted(reserve)

#     for r in reserve:
#         for l in lost:
#             if r == l:
#                 lost.remove(l)
#                 reserve.remove(r)

#             if r-1 == l or r+1 == l:
#                 answer += 1
#                 lost.remove(l)

#     return answer

# 다른 사람 풀이인데 2개 통과 못함
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)

# 위 풀이랑 뭐가 다르지??
def solution(n, lost, reserve):
    answer = []
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1) 
    answer = n-len(set_lost)
    return answer


n = 3
lost = [2,3]
reserve = [2,3]
print(solution(n, lost, reserve))