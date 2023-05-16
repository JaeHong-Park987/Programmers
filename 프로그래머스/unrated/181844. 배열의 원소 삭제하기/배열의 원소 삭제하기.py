def solution(arr, delete_list):
    answer = []
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer
#     for i in arr:
#         if i in delete_list:
#             arr.remove(i)
            
#     return arr