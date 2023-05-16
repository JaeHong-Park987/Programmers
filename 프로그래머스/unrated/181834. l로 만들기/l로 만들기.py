def solution(myString):
    before_l = ['a','b','c','d','e','f','g','h','i','j','k']
    answer = ''
    
    for i in myString:
        if i in before_l:
            answer += 'l'
        else:
            answer += i
            
    return answer