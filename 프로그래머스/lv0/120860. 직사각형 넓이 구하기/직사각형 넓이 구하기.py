def solution(dots):
    x = [] # x좌표 리스트
    y = [] # y좌표 리스트
    
    for c in dots:
        x.append(c[0])
        y.append(c[1])
        
    # 중복 제거
    x = list(set(x))
    y = list(set(y))
    
    w = abs(x[0] - x[1]) # 가로
    l = abs(y[0] - y[1]) # 세로
    area = w * l # 넓이
    
    return area