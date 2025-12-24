winner_points = 0

while True:
    player_name = input()
    if player_name == "Stop":
        break
    points = 0
    for char in player_name:
        number = int(input())
        ascii_value = ord(char)
        if number == ascii_value:
            points += 10
        else:
            points += 2
    if points >= winner_points:
        winner_points = points
        winner_name = player_name

print(f"The winner is {winner_name} with {winner_points} points!")
