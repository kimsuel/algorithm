"""
예제
number    limit    power    result
  5         3        2        10
  10        3        2        21
"""


def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1):
        count = 0
        sqrt = i ** 0.5
        for j in range(1, int(sqrt)+1):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1
            if count > limit:
                count = power
                break
        answer += count

    return answer


number = 10
limit = 3
power = 2
print(solution(number, limit, power))
