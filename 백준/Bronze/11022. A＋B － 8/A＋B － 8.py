import sys

t = int(sys.stdin.readline())

results = []
for i in range(1, t + 1):
    a, b = map(int, sys.stdin.readline().split())
    results.append(f"Case #{i}: {a} + {b} = {a + b}")
    
print("\n".join(results))