import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(n):
    if x > a[i]:
        result.append(a[i])
        
print(*result)