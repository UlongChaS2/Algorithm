import sys

n, m = map(int, sys.stdin.readline().split())
cards= list(map(int, sys.stdin.readline().split()))

cards.sort()
max_sum = 0

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            current_sum = cards[i] + cards[j] + cards[k]
            
            if current_sum <= m:
                if current_sum > max_sum:
                    max_sum = current_sum
            else:
                break

print(max_sum)