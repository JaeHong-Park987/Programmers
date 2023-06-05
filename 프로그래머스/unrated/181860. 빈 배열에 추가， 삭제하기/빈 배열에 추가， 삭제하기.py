def solution(arr, flag):
    X = []
    plus_list = []
    
    for i in range(len(arr)):
        if flag[i]:
            plus_list.append(arr[i])
            X.extend(plus_list * arr[i] * 2)
            plus_list = []
        else:
            del X[-arr[i]:]
              
    return X