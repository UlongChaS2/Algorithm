import math

def solution(num_list):
    if pow(sum(num_list), 2) > math.prod(num_list):
        return 1
    else:
        return 0