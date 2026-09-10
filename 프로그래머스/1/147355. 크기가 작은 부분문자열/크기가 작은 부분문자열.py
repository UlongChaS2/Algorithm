def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    count = 0
    
    for i in range(t_len - p_len + 1):
        if int(t[i:i+p_len]) <= int(p):
            count += 1 

    return count