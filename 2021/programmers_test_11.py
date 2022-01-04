def solution(genres, plays):
    answer = []
    # {장르 : 총 재생 횟수}
    playDict = {}
    # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
    genreDict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playDict[genre] = playDict.get(genre, 0) + play
        genreDict[genre] = genreDict.get(genre, []) + [(play, i)]

    # 재생 횟수 내림차순으로 장르별로 정렬
    genreSort = sorted(playDict.items(), key=lambda x: x[1], reverse=True)

    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        genreDict[genre] = sorted(
            genreDict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in genreDict[genre][:2]]

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
