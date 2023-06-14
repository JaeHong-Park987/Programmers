def solution(strArr):
    len_list = []
    count_list = []
    
    for i in strArr:
        len_list.append(len(i))
    
    for x in range(1, max(len_list)+1):
        count_list.append(len_list.count(x))
        
    return max(count_list)