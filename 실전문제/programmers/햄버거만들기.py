def solution(ingredient):
    answer = 0
    result = []

    for i in ingredient:
        result.append(i)
        if result[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                result.pop()

    return answer


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
