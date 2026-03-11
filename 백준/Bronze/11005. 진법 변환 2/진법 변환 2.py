import sys

n, b = map(int, sys.stdin.readline().split())
result = []
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n > 0:
    n, remainder = divmod(n, b)
    result.append(digits[remainder])

print("".join(result[::-1]))