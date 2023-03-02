def solution(array):
    counter = {}
    for value in array:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
            
    fre_list = list(counter.values())
    mode_fre = max(fre_list) # 최빈값 빈도
    # counter dict 뒤집기
    reverse = {v:k for k,v in counter.items()}
    mode = reverse.get(mode_fre)
    mode_list = [item for item in fre_list if item == mode_fre] # 최빈값 리스트
    
    if len(mode_list) == 1:
        answer = mode
    else:
        answer = -1
            
    return answer