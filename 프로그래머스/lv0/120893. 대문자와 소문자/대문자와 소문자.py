def solution(my_string):
    new = ''
    for i in my_string:
        if i.isupper():
            new += i.lower()
        else:
            new += i.upper()
            
    return new

# islower() -> 소문자인지 판별 / isupper() -> 대문자인지 판별