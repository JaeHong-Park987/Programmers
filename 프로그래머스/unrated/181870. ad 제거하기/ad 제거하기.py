def solution(strArr):
    answer = []
    for i in strArr:
        if i.find('ad') == -1:
            answer.append(i)
    
    return answer

# 문자열.find('찾고싶은문자열') -> 찾고 싶은 문자열이 전체 문자열에서 시작되는 인덱스를 출력
# 문자열에 찾고 싶은 내용이 없다면 -1 출력