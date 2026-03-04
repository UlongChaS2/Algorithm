import sys

n = int(sys.stdin.readline())
numbers_str = sys.stdin.readline().strip()

print(sum(int(s) for s in numbers_str))
    