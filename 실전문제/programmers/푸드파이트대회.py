def solution(food):
    answer = ''

    left = ''

    for i in range(1, len(food)):
        if food[i] != 0:
            for _ in range(0, food[i]//2):
                left += str(i)

    answer = left + "0"

    for i in range(len(left)-1, -1, -1):
        answer += left[i:i+1]

    return answer


# food = [1, 3, 4, 6]
food = [1, 7, 1, 2]
print(solution(food))
