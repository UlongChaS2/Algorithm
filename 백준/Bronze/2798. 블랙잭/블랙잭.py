import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0

for combo in combinations(cards, 3):
    current_sum = sum(combo)
    
    if current_sum <= m:
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)