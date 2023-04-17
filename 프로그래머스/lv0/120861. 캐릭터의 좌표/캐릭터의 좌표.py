def solution(keyinput, board):
    answer = [0,0]
    board[0] = board[0] // 2
    board[1] = board[1] // 2
    
    for k in keyinput:
        if k == 'left':
            answer[0] -= 1
        elif k == 'right':
            answer[0] += 1
        elif k == 'up':
            answer[1] += 1
        elif k == 'down':
            answer[1] -= 1
            
        while (abs(answer[0]) > board[0]):
            if answer[0] > 0:
                answer[0] -= 1
            elif answer[0] < 0:
                answer[0] += 1
            
        while (abs(answer[1]) > board[1]):
            if answer[1] > 0:
                answer[1] -= 1
            elif answer[1] < 0:
                answer[1] += 1
    return answer