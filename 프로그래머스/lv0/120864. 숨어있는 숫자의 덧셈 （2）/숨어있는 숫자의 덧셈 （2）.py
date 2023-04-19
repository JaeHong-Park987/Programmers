def solution(my_string):
    list = []
    str = ''
    total = 0
    for i in my_string:
        str += i
        if str.isdigit():
            list.append(str)
        else:
            str = ''
            list.append('*')
            
    for j in range(0, len(list)):
        if j < len(list)-1:
            if (list[j].isdigit()) & (list[j+1] == '*'):
                total += int(list[j])
        else:
            if list[j].isdigit():
                total += int(list[j])
    
    return total
        
        