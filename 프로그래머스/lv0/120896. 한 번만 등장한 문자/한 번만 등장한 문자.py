def solution(s):
    answer = ''
    
    for i in sorted(s):
        if sorted(s).count(i) == 1:
            answer += i
            
    return answer