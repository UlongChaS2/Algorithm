import sys

all_students = set(range(1, 31))

submitted = set(int(sys.stdin.readline()) for _ in range(28))

missing = all_students - submitted

for student in sorted(missing):
    print(student)