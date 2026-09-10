def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    p_num = int(p)

    return sum(1 for i in range(t_len - p_len + 1) if int(t[i:i+p_len]) <= p_num)