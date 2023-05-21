def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        answer += str(n).count(str(k))
        
    return answer

# count 함수를 통해 문자열에서 내가 원하는 문자의 수를 구할 수 있다.