student_name = input()
grade = 1
fail_count = 0
sum_grades = 0
grade_counter = 0

while grade <= 12:
    annual_grade = float(input())

    if annual_grade < 4.00:
        fail_count += 1
        if fail_count > 1:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue
    sum_grades += annual_grade
    grade_counter += 1
    grade += 1

if grade > 12 and fail_count <= 1:
    average = sum_grades / grade_counter
    print(f"{student_name} graduated. Average grade: {average:.2f}")
