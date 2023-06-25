def solution(my_string, queries):
    for query in queries:
        print(query[0], query[1])
        s = "".join(reversed(my_string[query[0]:query[1]+1]))        
        answer = my_string[:query[0]]+s+my_string[query[1]+1:]
        my_string = answer
    
    return answer
    