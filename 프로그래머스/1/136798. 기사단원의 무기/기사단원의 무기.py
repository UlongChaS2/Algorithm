def solution(number, limit, power):
    divisor_arr = []
    
    for num in range(1, number + 1):
        count = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                if i == num // i:
                    count += 1
                else:
                    count += 2
            i += 1
        divisor_arr.append(count)        
        
    for i in range(len(divisor_arr)):
        if divisor_arr[i] > limit:
            divisor_arr[i] = power
            
    return sum(divisor_arr)

            