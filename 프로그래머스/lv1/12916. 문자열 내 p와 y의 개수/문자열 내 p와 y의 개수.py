def solution(s):
    s = s.lower()
    p_count = 0
    y_count = 0
    
    for i in s:
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1
            
    if p_count == y_count:
        return True
    elif p_count != y_count:
        return False
    else:
        return True
        