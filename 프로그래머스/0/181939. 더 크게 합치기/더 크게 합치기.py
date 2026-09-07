def solution(a, b):
    sum_1 = str(a) + str(b)
    sum_2 = str(b) + str(a)
    
    if int(sum_1) > int(sum_2):
        return int(sum_1)
    else:
        return int(sum_2)