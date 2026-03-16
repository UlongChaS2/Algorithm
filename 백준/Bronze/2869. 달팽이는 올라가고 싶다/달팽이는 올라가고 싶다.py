import sys

a, b, v = map(int, sys.stdin.readline().split())

if (v - b) % (a - b) == 0:
    days = (v - b) // (a - b)
else:
    days = (v - b) // (a - b) + 1

print(days)