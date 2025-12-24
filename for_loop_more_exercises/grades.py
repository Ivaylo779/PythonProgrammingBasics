students = int(input())
top_students = 0
good_students = 0
satisfactory_students = 0
failed_students = 0
average = 0
# 10,3.00,2.99,5.68,3.01,4,4,6.00,4.50,2.44,5
for _ in range(1, students + 1):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        failed_students += 1
        average += grade
    elif 3.00 <= grade <= 3.99:
        satisfactory_students += 1
        average += grade
    elif 4.00 <= grade <= 4.99:
        good_students += 1
        average += grade
    elif 5.00 <= grade:
        top_students += 1
        average += grade

top_percentage = (top_students / students) * 100
good_percentage = (good_students / students) * 100
satisfactory_percentage = (satisfactory_students / students) * 100
failed_percentage = (failed_students / students) * 100
average_percentage = average / students

print(f"Top students: {top_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {good_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {satisfactory_percentage:.2f}%")
print(f"Fail: {failed_percentage:.2f}%")
print(f"Average: {average_percentage:.2f}")