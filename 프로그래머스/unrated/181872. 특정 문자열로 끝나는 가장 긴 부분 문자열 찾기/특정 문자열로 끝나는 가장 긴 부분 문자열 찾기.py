def solution(myString, pat):
    answer = ''
    a = []

    for i in myString:
        answer += i
        if pat in answer:
            a.append(answer)
            answer = ''
            
    result = ''       
    for i in a:
        result += i
            
    return result