def solution(s):
    answer = []

    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            location = s.rfind(s[i], 0, i)
            answer.append(i-location)

    return answer


s = "banana"
print(solution(s))
