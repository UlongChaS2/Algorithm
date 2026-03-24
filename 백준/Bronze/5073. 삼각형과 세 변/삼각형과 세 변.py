import sys

while True:
    angles = list(map(int, sys.stdin.readline().split()))
    a, b, c = angles
    
    if sum(angles) == 0:
        break
        
    angles.sort()
    
    if angles[2] >= angles[0] + angles[1]:
        print("Invalid")
    else:
        count = len(set(angles))
        if count == 1:
            print("Equilateral")
        elif count == 2:
            print("Isosceles")
        else:
            print("Scalene")
       
    