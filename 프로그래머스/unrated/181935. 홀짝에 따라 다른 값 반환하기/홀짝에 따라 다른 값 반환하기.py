def solution(n):
    answer = 0
    if n % 2 != 0: # 홀수라면
        for i in range(1,n+1,2): # 홀수만 추출하면 되기 때문에 1부터 n+1 까지 2+하면서 추출
            # if i % 2 != 0:
            answer += i
    else:
        for i in range(2, n+1 ,2): # 짝수만 추출하면 되기 때문에 2 부터 n+1 까지 2+ 하면서 추출
            # if i % 2 == 0:
            answer += i**2
                
    return answer