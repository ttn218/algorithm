grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

total_credit = 0
total_grade = 0

for _ in range(20):
    title, credit, grade = input().split(' ')
    
    if grade == 'P':
        continue
    
    total_credit += float(credit)
    total_grade += float(credit) * grade_dict[grade]
    
print(total_grade / total_credit)