def solution(a, b):

    return sum([x*y for x, y in zip(a, b)])


a = [-1, 0, 1]
b = [1, 0, -1]
print(solution(a, b))
