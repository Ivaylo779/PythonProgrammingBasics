floors = int(input())
rooms = int(input())

for number1 in range(floors, 0, -1):
    for number2 in range(rooms):
        if number1 == floors:
            print(f"L{number1}{number2}", end = " ")
            continue
        if number1 % 2 == 0:
            print(f"O{number1}{number2}", end = " ")
        else:
            print(f"A{number1}{number2}", end = " ")

    print()