male_clients = int(input())
female_clients = int(input())
max_tables = int(input())

occupied_tables = False

for person_1 in range(1, male_clients + 1):
    for person_2 in range(1, female_clients + 1):
        print(f"({person_1} <-> {person_2})", end = " ")
        max_tables -= 1
        if max_tables == 0:
            occupied_tables = True
            break
    if occupied_tables:
        break