def solution(s):
    answer = ''
    
    for i in sorted(s,reverse = True):
        answer += i
    
    return answer