def solution(my_string):
    suffix_list = []
    for i in range(len(my_string)):
        suffix_list.append(my_string[-i:])
    suffix_list.sort()
    
    return suffix_list