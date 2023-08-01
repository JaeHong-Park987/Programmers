def solution(a, b):
    dic = {1 : 'FRI',
           2 : 'SAT',
           3 : 'SUN',
           4 : 'MON',
           5 : 'TUE',
           6 : 'WED',
           0 : 'THU'}
    
    if a == 1: # 31
        return dic[b % 7]
    elif a == 2: # 29
        return dic[(31+b) % 7]
    elif a == 3: # 31
        return dic[(60+b) % 7]
    elif a == 4: # 30
        return dic[(91+b) % 7]
    elif a == 5: # 31
        return dic[(121+b) % 7]
    elif a == 6: # 30 
        return dic[(152+b) % 7]
    elif a == 7: # 31
        return dic[(182+b) % 7]
    elif a == 8: # 31
        return dic[(213+b) % 7]
    elif a == 9: # 30
        return dic[(244+b) % 7]
    elif a == 10: # 31
        return dic[(274+b) % 7]
    elif a == 11: # 30
        return dic[(305+b) % 7]
    elif a == 12: # 31
        return dic[(335+b) % 7]

# 31 29 31 30 31 30 31 31 30 31 30 31
# 366