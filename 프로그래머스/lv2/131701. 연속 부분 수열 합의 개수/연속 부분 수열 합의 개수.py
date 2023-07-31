def solution(elements):
    answer = []
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            answer.append(sum(elements[0:i]))
            elements.append(elements[0])
            elements.pop(0)
            
    answer = list(set(answer))
    
    return len(answer)