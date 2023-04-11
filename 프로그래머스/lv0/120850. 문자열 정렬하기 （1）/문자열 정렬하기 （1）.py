def solution(my_string):
    number = ["0","1","2","3","4","5","6","7","8","9"]
    answer = []
    for string in my_string:
        if string in number:
            answer.append(int(string))
    answer.sort()
    return answer

# isdigit을 사용하면 더 간단하다.
# def solution(my_string):
#     answer = []
#     for string in my_string:
#         if string.isdigit():
#             answer.append(int(string))
#     answer.sort()
    
#     return answer