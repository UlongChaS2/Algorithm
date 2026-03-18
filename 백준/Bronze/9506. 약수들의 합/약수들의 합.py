import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1: break
    
    factors = []
    
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            factors.append(i)
            if i != (n // i):
                factors.append(n // i)
                
    factors.sort()
    factors.pop()
    
    if sum(factors) == n:
        result_str = " + ".join(map(str, factors))
        print(f"{n} = {result_str}")
    else:
        print(f"{n} is NOT perfect.")