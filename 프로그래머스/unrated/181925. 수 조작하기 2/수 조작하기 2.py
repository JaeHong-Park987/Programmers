def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        b_num = numLog[i-1]
        a_num = numLog[i]
        
        if (a_num - b_num) == 1:
            answer += 'w'
        elif (a_num - b_num) == -1:
            answer += 's'
        elif (a_num - b_num) == 10:
            answer += 'd'
        elif (a_num - b_num) == -10:
            answer += 'a'
    
    return answer