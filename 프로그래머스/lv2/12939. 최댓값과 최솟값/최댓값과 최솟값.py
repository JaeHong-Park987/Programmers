def solution(s):
    num_list = s.split(' ')
    n_list = []
    
    for i in num_list:
        n_list.append(int(i))
        
    n_list.sort()
    
    return str(n_list[0]) + ' ' + str(n_list[-1])