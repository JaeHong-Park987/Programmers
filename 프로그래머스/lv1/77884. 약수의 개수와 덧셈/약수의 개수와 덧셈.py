def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        if int(i**0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    
    return answer
# 제곱수라면 약수의 수가 짝수이다.