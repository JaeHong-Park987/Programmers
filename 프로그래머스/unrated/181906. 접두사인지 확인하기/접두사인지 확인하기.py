def solution(my_string, is_prefix):
    prefix = [] # 접두사 리스트
    for i in range(len(my_string)):
        prefix.append(my_string[0:i+1])
        
    if is_prefix in prefix:
        return 1
    else:
        return 0