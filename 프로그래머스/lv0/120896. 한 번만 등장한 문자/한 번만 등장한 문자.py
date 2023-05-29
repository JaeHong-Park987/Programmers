def solution(s):
    answer = ''
    # sorted를 한 번만 사용 가능
    
    for i in sorted(s):
        if s.count(i) == 1: 
            answer += i
            
    return answer