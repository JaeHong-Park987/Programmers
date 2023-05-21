def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        dif = numLog[i] - numLog[i-1]
        
        if dif == 1:
            answer += 'w'
        elif dif == -1:
            answer += 's'
        elif dif == 10:
            answer += 'd'
        elif dif == -10:
            answer += 'a'
    
    return answer