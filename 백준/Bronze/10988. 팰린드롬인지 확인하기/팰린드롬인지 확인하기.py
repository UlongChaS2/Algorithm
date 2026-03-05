import sys

char = sys.stdin.readline().strip()
l = len(char)

for i in range(l // 2):
    if char[i] != char[-i - 1]:
        print(0)
        break
else:
    print(1)
    