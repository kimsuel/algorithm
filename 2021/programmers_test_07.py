# 신규 아이디 추천
import re


def solution(new_id):
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, 뺴기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)

    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) and new_id[len(new_id)-1] == '.':
        new_id = new_id[:-1]

    # 5. 빈 문자열이라면, new_id에 "a"를 대입
    if new_id == "":
        new_id = "a"

    # 6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[len(new_id)-1] == '.':
            new_id = new_id[:-1]

    # 7. 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다
    while len(new_id) <= 2:
        new_id += new_id[len(new_id)-1]

    return new_id


# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))
