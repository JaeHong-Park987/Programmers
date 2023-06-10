def solution(price, money, count):
    total = 0
    
    while count != 0 :
        total += price * count
        count -= 1
    
    lack_money = total - money
    
    if lack_money < 0:
        return 0
    else:
        return lack_money