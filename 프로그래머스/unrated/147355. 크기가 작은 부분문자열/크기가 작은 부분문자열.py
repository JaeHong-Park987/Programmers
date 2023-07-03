def solution(t, p):
    l = len(p)
    answer = 0
    
    for i in range(len(t)-l+1):
        if int(t[i:i+l]) <= int(p):
            answer += 1
    
    return answer