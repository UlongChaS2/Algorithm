import sys

t = int(sys.stdin.readline())
coins = [25, 10, 5, 1]

for _ in range(t):
    money = int(sys.stdin.readline())
    result = []
    
    for coin in coins:
        quotient, remainder = divmod(money, coin)
        result.append(quotient)
        money = remainder
        
    print(*result)
    