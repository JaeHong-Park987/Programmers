def solution(keyinput, board):
    answer = [0,0]
    board[0] = board[0] // 2
    board[1] = board[1] // 2
    
    for j in keyinput:
        if j == 'left' and answer[0] > -1 * board[0] :
            answer[0] -= 1
        elif j == 'right' and answer[0] < board[0] :
            answer[0] += 1
        elif j == 'up' and answer[1] < board[1] :
            answer[1] += 1
        elif j == 'down' and answer[1] > -1 * board[1] :
            answer[1] -= 1
            
#         while (abs(answer[0]) > board[0]):
#             if answer[0] > 0:
#                 answer[0] -= 1
#             elif answer[0] < 0:
#                 answer[0] += 1
            
#         while (abs(answer[1]) > board[1]):
#             if answer[1] > 0:
#                 answer[1] -= 1
#             elif answer[1] < 0:
#                 answer[1] += 1
    return answer