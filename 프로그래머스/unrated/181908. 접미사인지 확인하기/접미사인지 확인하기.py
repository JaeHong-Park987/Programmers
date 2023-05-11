def solution(my_string, is_suffix):
    # 전체 문자 길이에서 접미사 길이를 빼줘야 한다.
    if is_suffix in my_string[len(my_string) - len(is_suffix):]:
        return 1
    else:
        return 0
    
    # ex) banana -> len(my_string): 6 / na -> len(is_suffix): 2
    # my_string[6-2:] -> my_string[4:] = na