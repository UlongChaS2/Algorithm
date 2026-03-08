import sys

max_val = -1
row_idx = 0
column_idx = 0

for i in range(9):
    current_row = list(map(int, sys.stdin.readline().split()))
    row_max = max(current_row)
    
    if max_val < row_max or max_val < 0:
        max_val = row_max
        row_idx = i + 1
        column_idx = current_row.index(row_max) + 1
        
print(max_val)
print(row_idx, column_idx)
        
   
    
    