def solution(order):
    answer = 0
    for i in str(order):
        if int(i) != 0 and int(i) % 3 == 0: # i가 0이면 나머지가 0이기 때문에 0일 때도 카운트가 된다. 그러므로 i가 0이 아니면서 3으로 나눴을 때 나머지가 0일 때 카운트가 되야 한다.
            answer += 1
    
    return answer