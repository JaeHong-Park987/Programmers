def solution(my_string, s, e):
    answer = ''
    
    for i in range(len(my_string)):
        if s<= i <= e:
            answer += my_string[s+e-i]
        else:
            answer += my_string[i]

    return answer