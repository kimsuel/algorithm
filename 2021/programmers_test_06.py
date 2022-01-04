import copy


def solution(s):
    answer = 1001

    for i in range(1, len(s)):
        copy_string = copy.copy(s)
        get_count = check(copy_string, i)
        if answer > get_count:
            answer = get_count

    return answer


def check(copy_string, i):
    result_string = ''
    compare_string = ''
    count = 1

    for j in range(0, len(copy_string), i):
        if j+i >= len(copy_string):
            result_string += str(count) + \
                compare_string if compare_string == copy_string[j:j +
                                                                i] else compare_string

        if compare_string == copy_string[j:j+i]:
            count += 1
            continue
        result_string += str(count) + \
            compare_string if count != 1 else compare_string
        count = 1
        compare_string = copy_string[j:j+i]
    print(result_string)

    return len(result_string)


s = "abcabcdede"
print(solution(s))
