def solution(cacheSize, cities):
    cache_list = []
    answer_time = 0
    
    if cacheSize == 0:
        answer_time += len(cities) * 5
    else:
        for i in cities:
            cache_list.append(i.lower())
            if len(cache_list) == cacheSize+1:
                if cache_list[-1] in cache_list[:cacheSize]:
                    answer_time += 1
                    cache_list.remove(i.lower())
                else:
                    answer_time += 5
                    cache_list.pop(0)
            else:
                if len(cache_list) == 1:
                    answer_time += 5
                else:
                    if i.lower() in cache_list[:len(cache_list)-1]:
                        answer_time += 1
                    else:
                        answer_time += 5
    
    return answer_time
        