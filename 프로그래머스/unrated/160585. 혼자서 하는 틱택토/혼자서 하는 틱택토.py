def solution(board):
    answer = -1
    new_list = [] # 원소 값을 하나한 받아줄 새로운 리스트
    for i in range(0,3):
        for j in range(0, 3):
            new_list.append(board[i][j])
            
    if new_list.count('O') < new_list.count('X'): # 후공이 선공보다 많은 경우
        answer = 0
    elif (new_list.count('O') - new_list.count('X')) > 1:
        answer = 0
    elif ((new_list[0] == 'O' and new_list[1] == 'O' and new_list[2] == 'O') or
          (new_list[3] == 'O' and new_list[4] == 'O' and new_list[5] == 'O') or 
          (new_list[6] == 'O' and new_list[7] == 'O' and new_list[8] == 'O') or
          (new_list[0] == 'O' and new_list[3] == 'O' and new_list[6] == 'O') or
          (new_list[1] == 'O' and new_list[4] == 'O' and new_list[7] == 'O') or
          (new_list[2] == 'O' and new_list[5] == 'O' and new_list[8] == 'O') or
          (new_list[0] == 'O' and new_list[4] == 'O' and new_list[8] == 'O') or
          (new_list[2] == 'O' and new_list[4] == 'O' and new_list[6] == 'O')):
        if new_list.count('X') >= new_list.count('O'):
            answer = 0
        else:
            answer = 1
    elif ((new_list[0] == 'X' and new_list[1] == 'X' and new_list[2] == 'X') or
          (new_list[3] == 'X' and new_list[4] == 'X' and new_list[5] == 'X') or 
          (new_list[6] == 'X' and new_list[7] == 'X' and new_list[8] == 'X') or
          (new_list[0] == 'X' and new_list[3] == 'X' and new_list[6] == 'X') or
          (new_list[1] == 'X' and new_list[4] == 'X' and new_list[7] == 'X') or
          (new_list[2] == 'X' and new_list[5] == 'X' and new_list[8] == 'X') or
          (new_list[0] == 'X' and new_list[4] == 'X' and new_list[8] == 'X') or
          (new_list[2] == 'X' and new_list[4] == 'X' and new_list[6] == 'X')):
        if new_list.count('X') < new_list.count('O'):
            answer = 0
        else:
            answer = 1
    else:   
        answer = 1
        
    return answer
                
    