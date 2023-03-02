def solution(array):
    sort_arr = sorted(array)
    
    if len(array) % 2 != 0:
        answer = sort_arr[len(array) // 2]
        
    elif len(array) % 2 == 0:
        answer = (sort_arr[(len(array) // 2)] + sort_arr[(len(array) // 2) + 1]) // 2
        
    return answer