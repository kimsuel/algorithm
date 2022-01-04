def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(n):
    answer = []

    start = 1
    end = n

    while start < end/2:
        if n % start == 0:
            end = n // start
            if is_prime_number(start) and is_prime_number(end):
                answer = [start, end]
                break
        start += 1

    if len(answer) == 0:
        answer = [-1, -1]

    return answer


n = 12
print(solution(n))
