def solution(s):
    result = ''
    words = ''
    num_en = {'zero' : '0',
              'one' : '1',
              'two' : '2',
              'three' : '3',
              'four' : '4',
              'five' : '5',
              'six' : '6',
              'seven' : '7',
              'eight' : '8',
              'nine' : '9'}
    
    for i in s:
        if i in num_en.values():
            result += i
        else:
            words += i
            if words in num_en.keys():
                result += num_en[words]
                words = ''
    return int(result)