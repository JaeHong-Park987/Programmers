def solution(array):
    sort_arr = sorted(array)
    
    # array길이가 홀수일 때
    if len(array) % 2 != 0:
        answer = sort_arr[len(array) // 2]
    
    # array길이가 짝수일 때
    elif len(array) % 2 == 0:
        answer = (sort_arr[(len(array) // 2)] + sort_arr[(len(array) // 2) + 1]) // 2
        
    return answer