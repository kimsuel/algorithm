# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    leftH = [1,4,7]
    rightH = [3,6,9]
    choice = [2,5,8,0]
    currL = '*'
    currR = '#'

    for num in numbers:
        if num in leftH:
            currL
    return answer





numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
