import sys

n, b = sys.stdin.readline().split()
b = int(b)

result = 0
for char in n:
    if char.isdigit():
        val = int(char)
    else:
        val = ord(char) - 55
    
    result = result * b + val
    
print(result)