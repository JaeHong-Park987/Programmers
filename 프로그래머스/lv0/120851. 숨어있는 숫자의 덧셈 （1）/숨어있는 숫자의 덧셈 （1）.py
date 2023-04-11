def solution(my_string):
    answer = 0
    
    for str in my_string:
        if str.isdigit():
            answer += int(str)
            
    return answer