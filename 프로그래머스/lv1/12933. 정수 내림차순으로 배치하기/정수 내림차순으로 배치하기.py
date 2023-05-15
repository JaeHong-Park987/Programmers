def solution(n):
    l = list(str(n)) # 정수를 문자열로 바꾸고 리스트화 하기
    l.sort(reverse=True) # 리스트를 내림차순으로 정렬
    answer = ''
    for i in l:
        answer += str(i)
        
    return int(answer)