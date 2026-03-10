import sys

n, b = sys.stdin.readline().split()
b = int(b)

n = n[::-1]
result = 0

for i, char in enumerate(n):
    if char.isdigit():
        val = int(char)
    else:
        val = ord(char) - 55
    
    result += val * (b ** i)
    
print(result)