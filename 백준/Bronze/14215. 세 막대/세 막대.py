import sys

sides = list(map(int, sys.stdin.readline().split()))
sides.sort()


if sides[0] + sides[1] > sides[2]:
    print(sum(sides))
else:
    print((sides[0] + sides[1]) * 2 - 1)