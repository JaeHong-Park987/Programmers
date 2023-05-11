def solution(my_string, num1, num2):
    list_word = list(my_string)
    list_word[num1], list_word[num2] = list_word[num2], list_word[num1]
    answer = ''.join(list_word)
    
    return answer