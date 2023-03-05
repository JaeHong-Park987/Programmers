def solution(money):
    answer = []
    ice_americano = 5500
    buy = money // ice_americano
    charge = money % ice_americano
    answer.append(buy)
    answer.append(charge)
    return answer