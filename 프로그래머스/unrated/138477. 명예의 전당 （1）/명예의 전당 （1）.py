def solution(k, score):
    answer = []
    hof_list = []
    
    for i in score:
        hof_list.append(i)
        hof_list = sorted(hof_list, reverse = True)
        hof_list = hof_list[:k]
        answer.append(hof_list[-1])
    
    return answer