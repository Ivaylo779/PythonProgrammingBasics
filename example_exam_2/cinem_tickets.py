all_tickets = 0
students = 0
standard = 0
kids = 0

while True:
    film_name = input()
    if film_name == "Finish":
        break
    free_seats = int(input())
    student_tickets = 0
    standard_tickets = 0
    kids_tickets = 0
    occupied_seats = 0
    total_tickets = 0
    for _ in range(1, free_seats + 1):
        ticket_type = input()
        if occupied_seats > free_seats:
            break
        if ticket_type == "End":
            break
        if ticket_type == "student":
            students += 1
            student_tickets += 1
            occupied_seats += 1
        elif ticket_type == "standard":
            standard += 1
            standard_tickets += 1
            occupied_seats += 1
        elif ticket_type == "kid":
            kids += 1
            kids_tickets += 1
            occupied_seats += 1
    total_tickets += student_tickets + standard_tickets + kids_tickets
    percentage = total_tickets / free_seats * 100
    print(f"{film_name} - {percentage:.2f}% full.")
    all_tickets += total_tickets

print(f"Total tickets: {all_tickets}")
student_percentage = (students / all_tickets) * 100
print(f"{student_percentage:.2f}% student tickets.")
standard_percentage =( standard / all_tickets) * 100
print(f"{standard_percentage:.2f}% standard tickets.")
kids_percentage = (kids / all_tickets) * 100
print(f"{kids_percentage:.2f}% kids tickets.")