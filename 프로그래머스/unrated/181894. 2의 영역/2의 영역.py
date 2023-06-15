def solution(arr):
    index_list = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            index_list.append(i)
    
    if len(index_list) == 0:
        answer = [-1]
    elif len(index_list) == 1:
        answer = [arr[index_list[0]]]
    else:
        answer = arr[index_list[0] : index_list[-1]+1]
        
    return answer