import sys

n = int(sys.stdin.readline())

if n == 1:
    sys.exit()

d = 2
while d * d <= n:
    while n % d == 0:
        print(d)
        n //= d
    d += 1
    
if n > 1:
    print(n)