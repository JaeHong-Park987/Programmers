def solution(name, yearning, photo):
    dict1 = dict(zip(name, yearning))
    answer = []
    
    for p in photo:
        total_y = 0
        for i in p:
            if i in dict1:
                total_y += dict1[i]
        answer.append(total_y)
    return answer