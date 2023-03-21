def solution(my_string, letter):
    # answer = my_string.replace(letter, '')
    answer = ''
    for str in my_string:
        if str != letter:
            answer += str
    return answer