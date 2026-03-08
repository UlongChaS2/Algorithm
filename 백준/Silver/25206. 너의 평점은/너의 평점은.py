import sys

grade_map = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total_score = 0
total_credits = 0

for _ in range(20):
    line = sys.stdin.readline().split()
    if not line: break
    
    name, credit, grade = line[0], float(line[1]), line[2]
    
    if grade == "P":
        continue
        
    total_score += credit * grade_map[grade]
    total_credits += credit
    
print(f"{total_score / total_credits:.6f}")




