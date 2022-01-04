import re


def solution(registered_list, new_id):
    answer = ''

    if new_id not in registered_list:
        answer = new_id
    else:
        while True:
            if new_id not in registered_list:
                answer = new_id
                break
            alphas = re.findall('[a-zA-Z]+', new_id)
            numbers = re.findall('\d+', new_id)
            if len(numbers) == 0:
                n = 0 + 1
            else:
                n = int(numbers[0]) + 1
            n1 = str(n)
            new_id = alphas[0] + n1

    return answer


registered_list = ["apple1", "orange", "banana3"]
new_id = "apple"

print(solution(registered_list, new_id))
