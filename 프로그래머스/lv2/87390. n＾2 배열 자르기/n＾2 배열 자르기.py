def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        answer.append(max((i // n), (i % n)) + 1)
    
    return answer
#     k = 0
    
#     for i in range(n):
#         for j in range(n):
#             answer.insert(k,max(i,j)+1)
#             k += 1
    
#     return answer[left:right+1]