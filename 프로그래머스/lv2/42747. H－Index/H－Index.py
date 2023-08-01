def solution(citations):
    count_list = []
    
    for i in range(1, len(citations)+1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if i <= count:
            count_list.append(i)
    
    if len(count_list) == 0:
        return 0
    else:
        return max(count_list)