def solution(k, tangerine):
    new_dict = {}
    for i in tangerine:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    
    count_list = list(new_dict.values())
    count_list.sort(reverse = True)
    count = 0
    
    for n in count_list:
        k -= n
        count += 1
        if k <= 0:
            return count
        
# count 함수는 메모리를 많이 잡아 먹는다.