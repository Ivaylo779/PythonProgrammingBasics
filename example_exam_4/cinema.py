hall_capacity = int(input())
income = 0

while True:
    people = input()
    if people == "Movie time!":
        print(f"There are {hall_capacity} seats left in the cinema.")
        break
    people = int(people)
    if hall_capacity < people:
        print("The cinema is full.")
        break
    hall_capacity -= people
    income += people * 5
    if people % 3 == 0:
        income -= 5

print(f"Cinema income - {income} lv.")