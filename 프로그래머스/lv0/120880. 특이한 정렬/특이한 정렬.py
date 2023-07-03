def solution(numlist, n):
    answer = []
    dif_list = []
    numlist.sort()
    
    for i in numlist:
        new_list = []
        new_list.append(abs(i-n))
        new_list.append(i)
        dif_list.append(new_list)
    
    dif_list.sort(key=lambda x : (x[0], -x[1]))
    
    for k in dif_list:
        answer.append(k[1])
        
    return answer