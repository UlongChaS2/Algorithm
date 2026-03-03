import sys

score_len = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)

print(sum(s / max_score * 100 for s in scores)  / score_len)