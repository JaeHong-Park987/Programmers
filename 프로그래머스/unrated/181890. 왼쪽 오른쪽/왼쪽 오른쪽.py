def solution(str_list):
    answer = []
    
    for i in range(len(str_list)):
        # print(str_list[i], i)
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
    return []