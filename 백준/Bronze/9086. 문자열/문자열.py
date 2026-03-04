import sys

t = int(sys.stdin.readline())

for _ in range(t):
    string = sys.stdin.readline().strip()
    print(f"{string[0]}{string[-1]}")