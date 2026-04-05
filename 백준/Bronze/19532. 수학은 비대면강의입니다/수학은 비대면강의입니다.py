import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
denominator = a*e - b*d

if denominator != 0:
    x = (c*e - b*f) // denominator
    y = (a*f - c*d) // denominator
    print(x, y)