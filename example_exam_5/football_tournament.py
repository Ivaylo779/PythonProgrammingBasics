football_team_name = input()
matches_played = int(input())
points = 0
wins = 0
draws = 0
loses = 0

for _ in range(matches_played):
    match_result = input()
    if match_result == "W":
        points += 3
        wins += 1
    elif match_result == "D":
        points += 1
        draws += 1
    elif match_result == "L":
        loses += 1

if matches_played == 0:
    print(f"{football_team_name} hasn't played any games during this season.")
else:
    print(f"{football_team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    win_rate = (wins / matches_played) * 100
    print(f"Win rate: {win_rate:.2f}%")

