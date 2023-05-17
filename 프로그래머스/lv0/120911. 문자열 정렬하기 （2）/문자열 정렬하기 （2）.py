def solution(my_string):
    answer = ''
    
    for i in sorted(my_string.lower()):
        answer += i
    
    return answer