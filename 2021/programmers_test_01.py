# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    result_list = []
    count = 0
    
    for i in range(len(moves)):
        for j in range(len(board)):
            k = moves[i]-1
            if (board[j][k] != 0) :
                result_list.append(board[j][k])
                board[j][k] = 0
                count += 1
                if (count > 1 and result_list[count-1] == result_list[count-2]) :
                    answer += 2
                    del result_list[count-1]
                    del result_list[count-2]
                    count -= 2
                break
    
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))