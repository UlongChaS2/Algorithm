import sys

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().strip()

for char in croatia:
    word = word.replace(char, "*")
    
print(len(word))