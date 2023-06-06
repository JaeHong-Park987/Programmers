def solution(arr):
    count = 0
    
    while True:
        new_list = []
        for i in arr:
            if i < 50 and i % 2 != 0 :
                i = i * 2 + 1
                new_list.append(i)
            elif i >= 50 and i % 2 == 0:
                i = i / 2
                new_list.append(i)
            else:
                new_list.append(i)
        
        if arr == new_list:
            return count
        else:
            arr = new_list
            count += 1