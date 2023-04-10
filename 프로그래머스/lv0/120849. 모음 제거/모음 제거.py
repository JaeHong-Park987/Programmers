def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트
    answer = ''
    
    for i in my_string:
        if i not in vowel:
            answer += i
            
    return answer