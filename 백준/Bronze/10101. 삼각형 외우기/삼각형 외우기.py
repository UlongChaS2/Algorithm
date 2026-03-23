import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
angles = [a, b, c]

if sum(angles) != 180:
    print("Error")
else:
    count = len(set(angles))
    if count == 1: print("Equilateral")
    elif count == 2: print("Isosceles")
    else: print("Scalene")