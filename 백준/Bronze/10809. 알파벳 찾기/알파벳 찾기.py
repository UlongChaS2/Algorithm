import sys

s = sys.stdin.readline().strip()
print(*(s.find(chr(i)) for i in range(ord('a'), ord('z') + 1)))