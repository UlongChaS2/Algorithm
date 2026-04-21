import math

def solution(signals):
    info = []
    periods = []
    for g, y, r in signals:
        total = g + y + r
        info.append([total, g, g + y])
        periods.append(total)
    
    lcm = periods[0]
    for i in range(1, len(periods)):
        lcm = (lcm * periods[i]) // math.gcd(lcm, periods[i])

    for t in range(1, lcm + 1):
        all_yellow = True
        for total, yellow_start, yellow_end in info:
            current_pos = (t - 1) % total
            if not (yellow_start <= current_pos < yellow_end):
                all_yellow = False
                break
        
        if all_yellow:
            return t
            
    return -1