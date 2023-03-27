def solution(emergency):
    new_emergency = sorted(emergency) # 응급도 오름차순 정렬
    dict = {} # 응급도와 진료순서 딕셔너리
    order = [] # 진료 순서를 담을 리스트
    a = len(new_emergency) # 환자 수
    
    for i in new_emergency:
        dict[i] = a
        a -= 1
        
    for i in emergency:
        order.append(dict[i])
        
    return order