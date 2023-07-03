def solution(sizes):
    w_list = []
    l_list = []
    
    for s in sizes:
        w_list.append(max(s))
        l_list.append(min(s))
        
    return max(w_list) * max(l_list)