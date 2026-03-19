import sys

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())

print(sum(1 for x in numbers if is_prime(x)))