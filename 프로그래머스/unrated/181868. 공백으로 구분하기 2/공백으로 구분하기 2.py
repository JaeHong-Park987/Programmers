def solution(my_string):
    answer = []
    list = my_string.split(' ')
    for i in list:
        if i != '':
            answer.append(i)
            
    return answer