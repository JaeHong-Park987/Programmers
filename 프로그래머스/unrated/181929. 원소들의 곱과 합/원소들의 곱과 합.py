def solution(num_list):
    mul = 1 # 모든 원소의 곱 변수
    total = 0 # 모든 원소의 합 변수
    
    for i in num_list:
        mul *= i
        total += i
    
    total2 = total ** 2 # 합의 제곱
    
    if mul < total2:
        answer = 1
    else:
        answer = 0
    
    return answer