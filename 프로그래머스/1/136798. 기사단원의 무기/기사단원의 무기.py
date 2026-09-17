def solution(number, limit, power):
    divisor_arr = []
    
    for num in range(1, number + 1):
        count = sum(2 if i != num // i else 1 for i in range(1, int(num ** 0.5) + 1) if num % i == 0)
        divisor_arr.append(count)        
        
    for i in range(len(divisor_arr)):
        if divisor_arr[i] > limit:
            divisor_arr[i] = power
            
    return sum(divisor_arr)

            