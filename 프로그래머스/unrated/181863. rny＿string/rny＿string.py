def solution(rny_string):
#     answer = ''
#     for i in rny_string:
#         if i == 'm':
#             i = 'rn'
#             answer += i
#         else:
#             answer += i
            
#     return answer

# 간단하게 replace 함수를 사용하면 바꾸고 싶은 문자를 원하는 문자로 변경 가능하다.
    return rny_string.replace('m', 'rn')