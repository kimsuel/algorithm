def solution(s):
    numbers = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    for num in numbers:
        if num in s:
            s = s.replace(num, str(numbers.index(num)))

    return int(s)


s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"
print(solution(s))
