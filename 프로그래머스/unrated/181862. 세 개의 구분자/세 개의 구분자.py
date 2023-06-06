def solution(myStr):
    answer = []
    new_list = myStr.replace('a','c').replace('b','c').split('c')
    
    for i in new_list:
        if len(i) != 0:
            answer.append(i)
    if len(answer) == 0:
        return ['EMPTY']
    return answer