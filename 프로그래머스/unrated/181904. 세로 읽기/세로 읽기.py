def solution(my_string, m, c):
    answer = ''
    
    for i in range(0, len(my_string), m):
        answer += my_string[0+i:m+i][c-1]
    
    return answer