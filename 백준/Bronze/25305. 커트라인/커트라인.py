import sys

a, b = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort(reverse=True)
print(numbers[b - 1])