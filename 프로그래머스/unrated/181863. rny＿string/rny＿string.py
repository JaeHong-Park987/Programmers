def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i == 'm':
            i = 'rn'
            answer += i
        else:
            answer += i
            
    return answer