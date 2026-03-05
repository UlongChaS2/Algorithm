import sys

black = [1, 1, 2, 2, 2, 8]
white = list(map(int, sys.stdin.readline().split()))

print(*(b - w for b, w in zip(black, white)))
