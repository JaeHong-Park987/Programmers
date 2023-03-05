def solution(money):
    # 변수 선언
    answer = []
    ice_americano = 5500
    
    buy = money // ice_americano # 마실 수 있는 아메리카노의 잔 수
    charge = money % ice_americano # 남는 돈
    
    # 배열에 넣기
    answer.append(buy)
    answer.append(charge)
    
    return answer