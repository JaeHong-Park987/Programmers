def solution(myString):
    answer = ''
    
    for i in myString:
        if i < 'l': # 알파벳도 대소 비교가 가능하다
            answer += 'l'
        else:
            answer += i
            
    return answer