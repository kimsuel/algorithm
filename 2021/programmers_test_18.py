def solution(absolutes, signs):

    return sum([ab if si else -ab for ab, si in zip(absolutes, signs)])


absolutes = [1, 2, 3]
signs = [False, False, True]
print(solution(absolutes, signs))
