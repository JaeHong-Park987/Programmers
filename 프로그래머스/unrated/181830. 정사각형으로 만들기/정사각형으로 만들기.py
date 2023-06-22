def solution(arr):
    row = 0
    columns = len(arr[0])
    
    for i in arr:
        row += 1
        
    dif = abs(row-columns)
    
    if row > columns:
        for i in arr:
            for j in range(dif):
                i.append(0)
        return arr
    elif row < columns:
        for j in range(dif):
            arr.append([0] * columns)
        return arr
    else:
        return arr