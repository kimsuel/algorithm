def get_point(hand, alpha, gamer_points, game_point):
    index_list = [n for n in range(len(hand)) if hand.find(alpha, n) == n]
    for i in index_list:
        gamer_points[i] += game_point


def solution(n, m, points, hands):
    game_point = 0
    gamer_points = [0]*n

    for hand, point in zip(hands, points):
        p_count = hand.count('P')
        s_count = hand.count('S')
        r_count = hand.count('R')

        game_point += point

        if p_count == n or s_count == n or r_count == n or p_count == s_count == r_count:
            continue

        if p_count == 0 or s_count == 0 or r_count == 0:
            if game_point >= 0:
                if p_count == 0:
                    get_point(hand, 'R', gamer_points, game_point)
                elif s_count == 0:
                    get_point(hand, 'P', gamer_points, game_point)
                elif r_count == 0:
                    get_point(hand, 'S', gamer_points, game_point)
            else:
                if p_count == 0:
                    get_point(hand, 'S', gamer_points, game_point)
                elif s_count == 0:
                    get_point(hand, 'R', gamer_points, game_point)
                elif r_count == 0:
                    get_point(hand, 'P', gamer_points, game_point)
            game_point = 0
            continue

        if p_count != 0 and s_count != 0 and r_count != 0:
            if p_count == s_count:
                get_point(hand, 'R', gamer_points, game_point)
            elif s_count == r_count:
                get_point(hand, 'P', gamer_points, game_point)
            elif p_count == r_count:
                get_point(hand, 'S', gamer_points, game_point)
            else:
                if game_point >= 0:
                    max_count = max(p_count, s_count, r_count)
                    if p_count == max_count:
                        get_point(hand, 'R', gamer_points, game_point)
                    elif s_count == max_count:
                        get_point(hand, 'P', gamer_points, game_point)
                    elif r_count == max_count:
                        get_point(hand, 'S', gamer_points, game_point)
                else:
                    min_count = min(p_count, s_count, r_count)
                    if p_count == min_count:
                        get_point(hand, 'S', gamer_points, game_point)
                    elif s_count == min_count:
                        get_point(hand, 'R', gamer_points, game_point)
                    elif r_count == min_count:
                        get_point(hand, 'P', gamer_points, game_point)
            game_point = 0
            continue
      
    return max(gamer_points)

n = 6
m = 5
points = [5, -2, 1, 3, -5]
hands = ["PSPRSS", "SSRRSS", "RRRRRR", "RRSSPP", "SSSRRP"]

print(solution(n,m,points,hands))