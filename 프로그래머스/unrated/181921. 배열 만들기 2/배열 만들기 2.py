def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if ("1" not in str(i)) & ("2" not in str(i)) & ("3" not in str(i)) & ("4" not in str(i)) & ("6" not in str(i)) & ("7" not in str(i)) & ("8" not in str(i)) & ("9" not in str(i)):
            answer.append(i)
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer
            