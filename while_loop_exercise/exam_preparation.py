bad_mark_count = int(input())
bad_marks = 0
mark_sum = 0
mark_count = 0
exercise_count = 0
exercise_name = ""
last_problem = ""

while exercise_name != "Enough":
    exercise_name = input()
    if exercise_name == "Enough":
        break
    last_problem = exercise_name
    exercise_count += 1
    mark = int(input())
    mark_sum += mark
    mark_count += 1
    if mark <= 4.00:
        bad_marks += 1
    if bad_mark_count <= bad_marks:
        print(f"You need a break, {bad_marks} poor grades.")
        break

if exercise_name == "Enough":
    average = mark_sum / mark_count
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {exercise_count}")
    print(f"Last problem: {last_problem}")  
