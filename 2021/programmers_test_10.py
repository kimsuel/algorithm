# 해시 - 위장
def solution(clothes):
    answer = 1
    closet = {}

    for name, kind in clothes:
        closet.setdefault(kind, []).append(name)

    for value in closet.values():
        print(value)
        answer *= len(value) + 1

    return answer - 1


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
