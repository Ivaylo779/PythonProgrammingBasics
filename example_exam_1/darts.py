player_name = input()
full_points = 301
successful_shots = 0
unsuccessful_shots = 0

while True:
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
    points = int(input())
    if field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3

    if points > full_points:
        unsuccessful_shots += 1
        continue
    else:
        full_points -= points
        successful_shots += 1

    if full_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
