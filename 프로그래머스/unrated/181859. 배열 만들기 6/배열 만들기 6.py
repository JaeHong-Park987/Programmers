def solution(arr):
    answer = []
    
    for i in arr:
        if answer == []:
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
    
    if answer == []:
        return [-1]
    else:
        return answer